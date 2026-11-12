# joeysim-skills

A collection of agent skills. Each skill is a folder with a `SKILL.md` file in the [Agent Skills](https://agentskills.io/specification) format. The skills work in Claude Code, Codex, and other agents that support this format.

## Skills

| Skill | Use it when |
|-------|-------------|
| [Decision Matrix](skills/decision-matrix/SKILL.md) | Compare options, evidence, trade-offs, and unknowns to choose the next action. Keep a decision log in Markdown and HTML. |
| [I Lost the Plot](skills/i-lost-the-plot/SKILL.md) | Get a map of a long agent session when you lose track: the goal, the open loops, and the next step. |

## Install

Install all skills:

```sh
npx skills add joeysim/joeysim-skills
```

Install one skill:

```sh
npx skills add joeysim/joeysim-skills --skill <name>
```

These commands use the [skills CLI](https://github.com/vercel-labs/skills). They add the skills to the project in the current folder. Add `-g` to add them for your user account.

## Add a skill

Follow the steps in [AGENTS.md](AGENTS.md).

## License

MIT. See [LICENSE](LICENSE).

## Webpages

The [webpage template](templates/skill-page.html) holds the layout, the responsive styles, and these sections: a hero with the install command, a sample output with numbered notes, a second feature, steps, the install panel, and the full skill.
It uses plain HTML and CSS, and a short script for the Copy button, the theme switch, and the collapsed full skill. It has no external dependencies.
The page follows the system light or dark setting until the reader picks Light or Dark. The browser saves that choice.

Copy the template to `pages/<name>/index.html` for another skill.
Replace the sample headline, description, install command, ZIP filename, sample output, sections, and example.
Put every line of the skill's `SKILL.md` in the full skill section.
Keep navigation links consistent with section IDs.
Remove an optional section if the skill does not need it.

The [Decision Matrix page](pages/decision-matrix/index.html) contains the finished design.
The page uses static HTML. Update it when the skill instructions change.

The Pages workflow builds the download link and the ZIP for the live site. For a local preview, make them yourself. Git ignores both.

Create the raw download link once, from the repository root:

```sh
ln -s ../../skills/decision-matrix pages/decision-matrix/skill
```

Refresh the ZIP after you change the skill:

```sh
python3 -m zipfile -c pages/decision-matrix/decision-matrix.zip skills/decision-matrix
```

Preview the page:

```sh
python3 -m http.server 4316 --bind 127.0.0.1 --directory pages/decision-matrix
```

For another skill, replace `decision-matrix` with its folder name.

On each push to `main`, [the Pages workflow](.github/workflows/pages.yml) builds the downloads and publishes `pages/`.
The Decision Matrix page is at https://joeysim.github.io/joeysim-skills/decision-matrix/.
The I Lost the Plot page is at https://joeysim.github.io/joeysim-skills/i-lost-the-plot/.
Git ignores generated downloads and local runtime files.
