#!/usr/bin/env python3
"""Print a digest of a coding agent session: each user prompt, how each turn ended, and the git state.

The digest comes from the transcript on disk. It keeps the prompts that context compaction removed.

Usage:
    python3 session_digest.py [--session ID | --file PATH]
    python3 session_digest.py --self-test
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime

# shortcut: reads Claude Code transcripts only. Add a Codex rollout reader when Codex sessions need it.
PROJECTS = os.path.expanduser("~/.claude/projects")
RECENT_TURNS = 20  # Older turns get shorter text, so that a long session stays readable.
BUDGET = 22000  # Claude Code cuts tool output above 30,000 characters. The git state needs the rest.
# Text limits, tried in order until the digest fits: recent prompt, recent reply, older prompt, older reply.
LIMITS = [(1200, 600, 300, 160), (800, 400, 200, 100), (600, 300, 160, 70), (500, 300, 140, 0), (300, 200, 80, 0)]


def find_transcript(session):
    # No guess from the working folder: the newest transcript there can be a different session.
    # Other characters in the ID could match a different session, or a file outside the projects folder.
    if not session or not re.fullmatch(r"[\w-]+", session):
        return None
    hits = glob.glob(os.path.join(PROJECTS, "*", session + ".jsonl"))
    return hits[0] if hits else None


def text_of(message):
    content = (message or {}).get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text")
    return ""


def clip(text, limit):
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit // 2] + " [...] " + text[-limit // 2 :]


def local_time(stamp):
    try:
        return datetime.fromisoformat(stamp.replace("Z", "+00:00")).astimezone()
    except (AttributeError, ValueError):
        return None


def read_events(path):
    """Return (title, events). Each event is (time, kind, text). The kinds are user, queued, reply, interrupt, compact."""
    title, events = None, []
    with open(path, errors="replace") as lines:
        for line in lines:
            try:
                title = read_record(json.loads(line), events) or title
            except (ValueError, AttributeError, TypeError):
                continue  # The line is not JSON, or the record has a shape that this script does not know.
    return title, events


def read_record(rec, events):
    """Add the event of one transcript record to events. Return the session title when the record has it."""
    if rec.get("isSidechain"):
        return None
    kind, when = rec.get("type"), local_time(rec.get("timestamp"))
    if kind == "ai-title":
        return rec.get("aiTitle")
    if kind == "system" and rec.get("subtype") == "compact_boundary":
        events.append((when, "compact", ""))
    elif kind == "attachment":
        # The user typed this prompt while the agent worked.
        item = rec.get("attachment") or {}
        human = (item.get("origin") or {}).get("kind") == "human"
        if item.get("type") == "queued_command" and human and isinstance(item.get("prompt"), str):
            events.append((when, "queued", item["prompt"]))
    elif kind == "assistant":
        text = text_of(rec.get("message")).strip()
        if text:
            events.append((when, "reply", text))
    elif kind == "user" and not rec.get("isMeta") and not rec.get("isCompactSummary"):
        text = text_of(rec.get("message")).strip()
        origin = (rec.get("origin") or {}).get("kind")
        command = re.search(r"<command-name>(.*?)</command-name>", text)
        if text.startswith("[Request interrupted"):
            events.append((when, "interrupt", ""))
        elif command:
            args = re.search(r"<command-args>(.*?)</command-args>", text, re.S)
            events.append((when, "user", (command.group(1) + " " + (args.group(1) if args else "")).strip()))
        elif text and (origin == "human" or (origin is None and not text.startswith(("<", "[")))):
            # Transcripts from old versions have no origin field. There, harness text starts with a tag.
            events.append((when, "user", text))
    return None


def render(title, events):
    """Return the digest in the longest form that fits the budget."""
    for limits in LIMITS:
        text = render_with(title, events, limits)
        if len(text) <= BUDGET:
            return text
    head, _, rest = text.partition("\n\n")
    rest = rest[-BUDGET:]
    return head + "\n\nThe oldest lines do not fit. The digest starts later in the session.\n" + rest[rest.find("\n") + 1 :]


def render_with(title, events, limits):
    prompts = [i for i, e in enumerate(events) if e[1] in ("user", "queued")]
    compactions = sum(1 for e in events if e[1] == "compact")
    recent_from = prompts[-RECENT_TURNS] if len(prompts) > RECENT_TURNS else 0
    out = ["SESSION  " + (title or "(no title)")]
    out.append("PROMPTS  %d    COMPACTIONS  %d" % (len(prompts), compactions))
    if not prompts:
        out.append("No user prompts found. The transcript format is possibly different. Use the conversation context.")
    day = None
    for i, (when, kind, text) in enumerate(events):
        # Keep only the last reply of each turn: the reply before the next prompt, interrupt, or compaction.
        if kind == "reply" and i + 1 < len(events) and events[i + 1][1] == "reply":
            continue
        if when and when.date() != day:
            day = when.date()
            out.append("\n" + day.isoformat())
        clock = when.strftime("%H:%M") if when else "--:--"
        prompt_limit, reply_limit = limits[:2] if i >= recent_from else limits[2:]
        if kind == "user":
            out.append("%s  USER   %s" % (clock, clip(text, prompt_limit)))
        elif kind == "queued":
            out.append("%s  USER   (typed while the agent worked) %s" % (clock, clip(text, prompt_limit)))
        elif kind == "reply" and reply_limit:
            out.append("       AGENT  %s" % clip(text, reply_limit))
        elif kind == "interrupt":
            out.append("%s  -----  The user interrupted the agent here." % clock)
        elif kind == "compact":
            out.append("%s  -----  Context compacted here. The agent keeps only a summary of the lines above." % clock)
    return "\n".join(out)


def git(*args):
    try:
        done = subprocess.run(("git",) + args, capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.TimeoutExpired):
        return ""
    return done.stdout.strip() if done.returncode == 0 else ""


def git_state(since):
    status = git("status", "--short", "--branch")
    if not status:
        return "GIT  not a git repository"
    out = ["GIT  " + os.getcwd(), "\n".join(status.splitlines()[:40])]
    stashes = git("stash", "list").splitlines()
    if stashes:
        out.append("STASHES  %d (git shares stashes between worktrees)\n%s" % (len(stashes), "\n".join(stashes[:5])))
    if since:
        log = git("log", "--since=" + since.isoformat(), "--format=%h %ad %s", "--date=format:%m-%d %H:%M")
        out.append("COMMITS SINCE THE SESSION START\n" + ("\n".join(log.splitlines()[:30]) or "none"))
    return "\n".join(out)


def self_test():
    def rec(kind, text=None, **extra):
        base = {"type": kind, "timestamp": "2026-01-02T10:00:00.000Z"}
        if text is not None:
            base["message"] = {"content": text}
        base.update(extra)
        return json.dumps(base)

    lines = [
        rec("ai-title", aiTitle="Stock CLI"),
        rec("user", "Build the CLI", origin={"kind": "human"}),
        rec("user", [{"type": "tool_result", "content": "ok"}]),
        rec("user", "Base directory for this skill", isMeta=True),
        rec("assistant", [{"type": "text", "text": "Working on it."}]),
        rec("assistant", [{"type": "tool_use", "name": "Bash"}]),
        rec("attachment", attachment={"type": "queued_command", "prompt": "also add a json flag", "origin": {"kind": "human"}}),
        rec("attachment", attachment={"type": "queued_command", "prompt": "<task-notification>", "origin": {"kind": "task-notification"}}),
        rec("assistant", [{"type": "text", "text": "Built it. " + "x" * 2000 + " Tests pass."}]),
        rec("assistant", [{"type": "text", "text": "Sidechain text"}], isSidechain=True),
        rec("system", subtype="compact_boundary"),
        rec("user", "This session is being continued", isCompactSummary=True),
        rec("user", "<task-notification>done</task-notification>", origin={"kind": "task-notification"}),
        rec("user", "<command-name>/review</command-name><command-args>the diff</command-args>"),
        rec("user", "<local-command-stdout>Set model</local-command-stdout>"),
        rec("user", [{"type": "text", "text": "[Request interrupted by user]"}]),
        rec("user", "An old prompt with no origin field"),
        "not json",
        # Records with a shape that the script does not know. The script must skip them.
        "[1, 2]",
        "null",
        rec("attachment", attachment="text"),
        rec("attachment", attachment={"type": "queued_command", "prompt": ["a", "list"], "origin": {"kind": "human"}}),
        json.dumps({"type": "user", "message": "a string", "origin": "human"}),
        json.dumps({"type": "assistant", "message": {"content": [None, 7, {"type": "text", "text": 5}]}}),
    ]
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as handle:
        handle.write("\n".join(lines))
    try:
        title, events = read_events(handle.name)
    finally:
        os.unlink(handle.name)
    text = render(title, events)
    assert title == "Stock CLI", title
    assert [e[1] for e in events] == [
        "user", "reply", "queued", "reply", "compact", "user", "interrupt", "user",
    ], [e[1] for e in events]
    assert "PROMPTS  4    COMPACTIONS  1" in text, text
    assert "USER   Build the CLI" in text
    assert "(typed while the agent worked) also add a json flag" in text
    assert "USER   /review the diff" in text
    assert "USER   An old prompt with no origin field" in text
    assert "The user interrupted" in text and "Context compacted" in text
    assert "Built it." in text and "Tests pass." in text and "x" * 700 not in text
    for noise in ("tool_result", "Base directory", "Sidechain text", "task-notification", "Set model", "being continued"):
        assert noise not in text, noise
    assert "No user prompts found" in render(None, [])
    for bad in ("*", "../x", "a/b", "", None):
        assert find_transcript(bad) is None, bad
    # A long session must fit the budget and keep its newest prompt.
    stamp = datetime(2026, 1, 2, 10, 0).astimezone()
    many = [(stamp, "user", "prompt %d " % n + "y" * 400) for n in range(600)]
    long_text = render("Long", many)
    assert len(long_text) <= BUDGET + 200, len(long_text)
    assert "prompt 599 " in long_text and "prompt 0 " not in long_text and "do not fit" in long_text
    print("self-test passed")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--session", default=os.environ.get("CLAUDE_CODE_SESSION_ID"), help="session ID")
    parser.add_argument("--file", help="path of a transcript file")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    path = args.file or find_transcript(args.session)
    since = None
    try:
        title, events = read_events(path) if path else (None, None)
    except OSError:  # No file, a folder, or no permission to read.
        events = None
    if events is None:
        print("No transcript found. Use the conversation context.")
    else:
        print(render(title, events))
        since = next((e[0] for e in events if e[0]), None)
    print("\n" + git_state(since))


if __name__ == "__main__":
    sys.exit(main())
