# Visual output

These rules apply to visual output, such as HTML.
They add to the rules in "Present the matrix" in `SKILL.md`.
The bundled `scripts/render_html.py` already follows them for the decision log.

## Columns and chips

Give option columns equal widths across all visual tables.
Use a compact, rounded chip for **Recommended** or **Selected**.
Put the chip in a row above the option titles, centered over its column.
Start all option titles at the same height.
Use a neutral or blue chip style that differs from the rating colors.
For **Selected**, invert the **Recommended** chip: use its text color as the fill, and its fill color as the text.

## Option headers

Show option titles in the text color, with a dotted underline for each link, as for the evidence IDs.
Show each description beneath its title, in smaller, regular-weight gray text.
Keep descriptions aligned with their option columns.

## Layout and color

Show previews only when they represent the compared variants.
Keep text readable at narrow widths.
Show the key fact of each cell on its own line, in regular weight.
Show the basis and the evidence IDs below it, in smaller, fainter text.
Link each evidence ID to its reference.
Open links to pages outside the decision log in a new tab.
Show the `## Evidence` and `## References` sections in smaller gray text.
Use black text on light surfaces and responsive font sizes.
Use clear traffic-light colors.
Use green for Supported, yellow for Partial, and red for Not supported.
Keep color fills distinct from the page background.
Show a color key below the matrix.
Keep Unknown gray or uncolored.
Use yellow for Simulated with an explicit provisional label.
Do not represent missing evidence as an observed middle outcome.
Put a border around the recommended column and its chip.
Colors and layout do not establish evidence quality.
