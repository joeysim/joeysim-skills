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
- When you change a skill, update `pages/<name>/index.html` to match. Then refresh the ZIP, as in the "Webpages" section of `README.md`.

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
4. Add a row for the skill to the table in `README.md`.
5. Make a page for the skill. Follow the "Webpages" section of `README.md`.
6. Commit the skill and its page. Then tag the commit, as in "Versions".

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
