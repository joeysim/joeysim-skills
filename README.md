# joeysim-skills

A collection of agent skills. Each skill is a folder with a `SKILL.md` file in the [Agent Skills](https://agentskills.io/specification) format. The skills work in Claude Code, Codex, and other agents that support this format.

## Skills

| Skill | Use it when |
|-------|-------------|
| [Decision Matrix](skills/decision-matrix/SKILL.md) | Compare options, evidence, trade-offs, and unknowns to choose the next action. Keep a decision log in Markdown and HTML. |

## Install

Install all skills:

```sh
npx skills add joeysim/joeysim-skills
```

Install one skill:

```sh
npx skills add joeysim/joeysim-skills --skill <name>
```

## Add a skill

Follow the steps in [AGENTS.md](AGENTS.md).

## License

MIT. See [LICENSE](LICENSE).

## Webpages

The [webpage template](templates/skill-page.html) preserves the layout, navigation, responsive styles, and optional comparison components.
It uses plain HTML and CSS without external dependencies.

Copy the template to `pages/<name>/index.html` for another skill.
Replace the sample title, description, invocation, download filename, sections, and example.
Keep navigation links consistent with section IDs.
Remove the comparison table if the skill does not need one.

The [Decision Matrix page](pages/decision-matrix/index.html) contains the finished design.
The page uses static HTML. Update it when the skill instructions change.

Create the raw download link once, from the repository root:

```sh
ln -s ../../skills/decision-matrix pages/decision-matrix/skill
```

Refresh the ZIP after changing the skill:

```sh
python3 -m zipfile -c pages/decision-matrix/decision-matrix.zip skills/decision-matrix
```

Preview the page:

```sh
python3 -m http.server 4316 --bind 0.0.0.0 --directory pages/decision-matrix
```

For another skill, replace `decision-matrix` with its folder name.

On each push to `main`, [the Pages workflow](.github/workflows/pages.yml) builds the downloads and publishes `pages/`.
The Decision Matrix page is at https://joeysim.github.io/joeysim-skills/decision-matrix/.
Git ignores generated downloads and local runtime files.
