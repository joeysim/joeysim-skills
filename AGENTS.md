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
- When you change a skill, update `pages/<name>/index.html` to match. Then refresh the ZIP, as in the "Webpages" section of `README.md`.

## Add a skill

1. Create `skills/<name>/SKILL.md` with this frontmatter:

   ```markdown
   ---
   name: <name>
   description: Use when <the situations that call for this skill>.
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
6. Commit the skill and its page.
