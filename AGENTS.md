# AGENTS.md

This repo holds agent skills in the [Agent Skills](https://agentskills.io/specification) format. Each skill is one folder in `skills/`.

## Layout

```
skills/
  <name>/
    SKILL.md      required
    references/   optional: long reference text that SKILL.md links to
    scripts/      optional: helper scripts
    assets/       optional: templates and other files
    agents/       optional: agent metadata, such as openai.yaml for Codex
pages/
  index.html      the site root: a sheet for each skill
  <name>/
    index.html    required: the web page for the skill
templates/
  skill-page.html the starting point for a new page
```

## Rules for a skill

- Make the folder name the same as the `name` field in the frontmatter.
- Use 1 to 64 characters for `name`: lowercase letters, digits, and single hyphens.
- Write `description` in the third person, in 1024 characters or fewer.
- Start `description` with "Use when". Tell when to use the skill, not the steps it follows.
- Keep `SKILL.md` under 500 lines. Move long reference text to `references/`.
- Run bundled scripts through their interpreter, such as `python3 scripts/tool.py`. Some installers remove the executable bit.
- When you change a file in a skill folder, increase the skill's version in the same commit. Follow the rules in "Versions".
- When you change a skill, update `pages/<name>/index.html` to match. Put every line of `SKILL.md` in the page's full skill section.
- Show the skill's version in the page's hero and footer.
- Keep the styles and the script of each page the same as in `templates/skill-page.html`. When you change one, change the template and every page.
- The decision-log pages get their styles and theme switch from `skills/decision-matrix/scripts/render_html.py`. When you change the theme colors or the switch, change that script too.

## Add a skill

1. Create `skills/<name>/SKILL.md` with this frontmatter:

   ```markdown
   ---
   name: <name>
   description: Use when <the situations that call for this skill>.
   metadata:
     version: "1.0.0"
   ---
   ```

2. Link the skill into your agents, so that your edits are live. Run these commands from the repo root:

   ```sh
   ln -s "$PWD/skills/<name>" ~/.claude/skills/<name>   # Claude Code
   ln -s "$PWD/skills/<name>" ~/.agents/skills/<name>   # Codex and other agents
   ```

3. Test the skill on a real task. Compare the result with the same task without the skill. The `superpowers:writing-skills` skill gives a full test process.
4. Add a row for the skill to the table in `README.md`, and a sheet for it to `pages/index.html`.
5. Make a page for the skill. Follow the "Webpages" section of `README.md`.
6. Commit the skill and its page. Then tag the commit, as in "Versions".

## Test a skill change

- Run each test agent in a new folder outside this repo, such as a scratch folder with `git init`. An agent that starts in this repo can read the skill files without loading the skill.
- Give the test folder a neutral name. A folder named "baseline" made an agent skip the skill.
- Check the agent's transcript for a call to the skill. A result without that call does not test the skill.
- Let the test agent read the skill folder. An agent that cannot open the reference files does not test their rules.
- A test agent can get a copy of `SKILL.md` that is older than your latest edit. Check which rules the agent followed.
- Keep test output in `.local/`. Git ignores that folder.
- After a change to a bundled script, run its self-test, such as `python3 skills/decision-matrix/scripts/render_html.py --self-test`.
- Run each bundled script on bad input: an empty file, a file in the wrong format, a missing file, and a folder. Add each failure to the self-test.
- To test a skill that reads the session history, fork a session: `claude -p "<phrase>" --resume <session-id> --fork-session`. The original session does not change. Delete the transcript of the fork after the test.

### Optional checks with skill-creator-plus

[skill-creator-plus](https://github.com/yaniv-golan/skill-creator-plus) has checks that this repo does not have. These steps were checked with its version 0.18.0.
Clone it outside this repo. Run its scripts from its `skill-creator-plus/skills/skill-creator-plus/` folder:

```sh
python3 -m scripts.quick_validate <skill folder>
python3 -m scripts.check_portability <skill folder> --target all --strict
python3 -m scripts.run_eval --eval-set <queries.json> --skill-path <skill folder> --model <model ID> --timeout 60
```

- `quick_validate` checks the frontmatter and the folder name.
- `check_portability` finds text that can fail in other runtimes. It matches words, so read each finding before you change the skill.
- `run_eval` measures how often `description` triggers the skill. Run it after you change `description`. Write about 10 queries that must trigger the skill, and about 10 near misses that must not.
- `run_eval` hides your installed skills only when `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN` is set. Without one, a call to an installed skill stops the run with no score.
- Without a credential, put a wrapper named `claude` first on `PATH`. The wrapper runs the real CLI with `--setting-sources project --strict-mcp-config --no-session-persistence`.
- Each `run_eval` query leaves a `*-skill-trigger-eval-*` folder in `~/.claude/projects/`. Remove these folders after the run.

## Versions

Each skill has its own version in [Semantic Versioning](https://semver.org) format: MAJOR.MINOR.PATCH.
Put the version in `metadata.version` in the frontmatter, as a quoted string. The Agent Skills format has no top-level `version` field.
Start a new skill at 1.0.0.

Increase one part of the version for each change to the skill folder:

| Change | Part | Examples |
|--------|------|----------|
| Users must change how they use the skill, or output that they rely on changes. | MAJOR | Rename the skill. Remove a capability. Change the output format. Make the skill trigger in fewer situations. |
| The skill does something new or different, and old requests still work. | MINOR | Add or change a rule. Add a reference file. Make the skill trigger in more situations. |
| The behavior stays the same. | PATCH | Fix wording, a typo, or an example. |

When you increase a part, set the parts after it to 0. For example, 1.4.2 becomes 1.5.0 or 2.0.0.
Changes outside the skill folder, such as its page or the README, do not change the version.

After you push the change, tag the commit and push the tag:

```sh
git tag decision-matrix/v1.1.0
git push origin decision-matrix/v1.1.0
```

Do not move or delete a tag after you push it.
