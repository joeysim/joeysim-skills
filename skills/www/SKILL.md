---
name: www
description: Use when the user says that they lost the plot, lost track, or lost the thread of the current coding agent session, such as "where were we", "where are we", "I lost the plot", "I completely lost the plot", "what was I doing", "catch me up", or "what is still open". Also use when the user asks which threads or loops are open in the session, or asks for the i-lost-the-plot skill.
metadata:
  version: "1.1.0"
---

# Where Were We

The user lost track of this session.
Show where the session was headed, which threads are open, and the next step.

The user's words are about the full session, not about your last answer. Do not explain the last answer again.

Only read. Do not edit files, run tests, or continue a task until the user replies to the plot.

## 1. Get the evidence

Run the digest script from the user's working folder:

```sh
python3 <skill folder>/scripts/session_digest.py
```

The script prints each user prompt with its time, and the end of each agent turn.
It reads the session transcript on disk. Thus it also shows the prompts that context compaction removed.
It also prints the git state: the branch, the changed files, the stashes, and the commits since the session start. Do not run git again.
Read the full output. Do not cut it with `head` or `tail`. The script keeps the output short.
When the script cannot run or finds no transcript, use the conversation context and run `git status --short --branch`.

The script cannot see the task list, background tasks, or subagents. Check those too, when available.

## 2. Find the threads

A thread is one line of work: a request, a question, a problem, or a side idea.
Read the digest from the first prompt to the last. Give each thread one status:

| Mark | Status | Meaning |
|------|--------|---------|
| `▶` | now | The work that was in progress at the last prompt. |
| `○` | open | Requested or started, and not finished. |
| `?` | needs you | Waits for an answer or a decision from the user. |
| `✓` | done | Finished, with evidence in the session or in git. |
| `✗` | dropped | The user canceled it or replaced it. |

Look for these open loops. The user forgets them first:

- A request that the user made in passing: "also", "later", "at some point", "remind me".
- A prompt that the user typed while the agent worked.
- A question from the agent that the user did not answer.
- A question from the user that the agent did not answer.
- A task that an interruption or a new request stopped.
- A step that the agent promised and did not do.
- A problem that the agent found and did not fix: a failing test, an error, an unverified claim.
- Work that is not committed, not pushed, or in a stash. A branch that is not merged.

Use only what the session and the workspace show. Do not invent a thread.
When only the agent's own words say "done", and git or a test result disagrees, mark the thread open.

## 3. Show the plot

Print these four parts, in this order, and nothing else. Keep the answer to 30 lines or fewer.

1. One sentence that starts with "You set out to". Use the user's own words where possible.
2. One sentence that starts with "Right now". Tell where the work is.
3. The thread map, in a code block. The map shows each thread and each open loop. Do not add a list of loops below it.
4. One line that starts with "Next:", with one recommended step and the reason. Then the last line: `Say "go" to start that, a number to pick a different loop, or "drop 3" to close a loop.` Use a number from the map.

The map is a tree:

- The first line is the session goal, with no mark. When the goal changed during the session, use the latest goal.
- The next level shows the threads of that goal, in the order that they started.
- Indent a thread below the thread that caused it: its parts, its side tasks, and its open loops.
- Put a loop at the top level only when no thread caused it.
- Show the earlier goals as one `✓` thread, such as `✓ Earlier: repo setup, 1.4.0, 1.5.0`. Put their open loops below it.

Each line has a mark and a name. Some lines also have a note:

| Mark | Name | Note |
|------|------|------|
| `○` | A number, then the action that closes the loop. Start with a verb. | The state or the evidence: a time, a quote, a file, or a result. |
| `?` | A number, then the question. | The replies that answer it, such as `say "2 tenant" or "2 key"`. |
| `▶` | The work in progress. | `← you are here` |
| `✓` or `✗` | The work that is done or dropped. | No note. |

- Number the loops from 1, from the top of the map to the bottom.
- Use six words or fewer for a name, and eight words or fewer for a note.
- Align the notes in one column. Keep each line to 90 characters or fewer.
- Use `▶` one time at most.
- Show work that is not committed or not pushed as one `○` thread.
- Show seven loops at most. Keep the loops of the latest goal, then the most important older loops.
- When more loops exist, add one last line below the earlier goals: `○ + 4 older loops`, with the note `say "more"`.
- When the map has more than 15 lines, join the `✓` lines of one level into one line, such as `✓ 5 smaller fixes`.
- End the block with an empty line and the legend line.

## 4. Act on the reply

| Reply | Action |
|-------|--------|
| "go" | Do the step from the "Next:" line. |
| A number | Continue that loop. First tell what is left, in one or two sentences. |
| A number and an answer, such as "2 key" | Use the answer for that `?` loop. Then continue the work that waited for it. |
| "drop" and a number | Mark that loop as dropped. Change nothing: no edits, no reverts, no deletes. |
| "more" | Show the older loops as a map in the same format, with new numbers. Use one `✓` thread for each earlier goal, with its loops below it. |

Start the answer with the name of the loop, such as "Loop 3, docs for the new headers:".
The numbers change with each plot. The name keeps the transcript clear for the next plot.

## Example

You set out to "stop the 429 storms" on the API gateway before Friday.
Right now the Redis counters are half done, and one test still fails.

```
Rate limits for the API gateway
├─ ✓ Token bucket middleware
├─ ▶ Redis counters                      ← you are here
│  └─ ○ 1  Fix the flaky counter test    fails 1 run in 5, cause is a guess
├─ ? 2  Limits per tenant or per key?    say "2 tenant" or "2 key"
├─ ○ 3  Write docs for the new headers   you said "later" at 13:40
├─ ✗ Limits in nginx
└─ ○ 4  Commit four changed files        branch rate-limit, last commit 13:55

▶ now   ○ open   ? needs you   ✓ done   ✗ dropped
```

Next: finish the Redis counters, because loop 1 is probably the same bug.
Say "go" to start that, a number to pick a different loop, or "drop 3" to close a loop.
