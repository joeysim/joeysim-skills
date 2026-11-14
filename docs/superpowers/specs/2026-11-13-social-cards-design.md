# Social preview cards

## Intent

A link to a page of the site must show a preview image when someone shares it on X, LinkedIn, Slack, Discord, or iMessage. The image shows what the skill makes. For example, the Decision Matrix card shows a rated matrix.

## Goals

- Each page has a 1200×630 PNG preview: the site root, `decision-matrix`, and `www`.
- The redirect page `i-lost-the-plot` uses the `www` image.
- Each card is readable at the size of a feed thumbnail.

## Non-goals

- The GitHub repo social preview. Only the repo settings page can set it. The user can upload the root card there.
- A version number on the cards. Then a release does not make a card out of date.
- Automatic rendering in the Pages workflow.

## Approaches

1. Card page for each skill, rendered by headless Chrome. Picked by the user.
2. Screenshot of the sample on the live page. Rejected: the matrix text is too small at preview size, and a page layout change can break the crop.
3. Draw each image with PIL. Rejected: more code, and the result looks less like the site.

## Design

- `cards/<name>.html` is the source of each card. `cards/index.html` is the root card. The folder is outside `pages/`, so the Pages workflow does not publish the card sources.
- Each card is one HTML file at 1200×630. The cards share `cards/card.css`, which has the light colors and the fonts of `templates/skill-page.html`.
- Each card shows "joeysim-skills", the page headline, and a short copy of the page sample. The `decision-matrix` card has three options and three criteria. The `www` card has a cut-down thread map. The root card shows the two skills.
- `cards/render.sh` runs headless Chrome on each card. It writes `pages/og.png` and `pages/<name>/og.png`.
- Each page gets `og:image` (absolute URL), `og:image:width`, `og:image:height`, and `og:image:alt`. X uses `og:image`, so the pages need no `twitter:image`. `twitter:card` changes to `summary_large_image`. The template gets the same lines.
- AGENTS.md tells how to render the cards again, and when: after a change to a headline or a sample.

Sketch of the Decision Matrix card:

```
+------------------------------------------------------------+
| joeysim-skills                                             |
|                                                            |
| Decision Matrix                                            |
| Make your agent show its work.                             |
|                                                            |
|            | A. Current | B. Guided [Recommended] | C. ... |
| Offline    |  green     |  green                  |  red   |
| Cost       |  green     |  green                  |  red   |
| Fewer fixes|  gray      |  yellow                 |  gray  |
+------------------------------------------------------------+
```

## Left to the builder

- The exact text size, spacing, and the crop of each sample.
- The Chrome flags. Check that the PNG is exactly 1200×630.
