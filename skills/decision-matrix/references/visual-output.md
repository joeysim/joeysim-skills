# Visual output

These rules apply to visual output, such as HTML.
They add to the rules in "Present the matrix" in `SKILL.md`.
The bundled `scripts/render_html.py` already follows them for the decision log.

## Columns and chips

Give option columns equal widths across all visual tables.
Keep those widths stable when descriptions expand or collapse.
Use a compact, rounded chip for **Recommended** or **Selected**.
Use a neutral or blue chip style that differs from the rating colors.
For **Selected**, invert the **Recommended** chip: use its text color as the fill, and its fill color as the text.

## Option descriptions

Show descriptions expanded by default, with a downward arrow at the left of the sentence.
Put a left border between the arrow and the sentence.
Do not put the arrow on a line of its own.
Collapse the sentence when the user activates the arrow or the sentence.
Show Description beside a right-pointing arrow only when collapsed.
Expand the sentence when the user activates that control.
Use smaller, regular-weight text with readable contrast.
Keep description controls usable with a keyboard and on touch screens.
Keep descriptions aligned with their option columns.

## Layout and color

Show previews only when they represent the compared variants.
Keep text readable at narrow widths.
Use black text on light surfaces and responsive font sizes.
Use clear traffic-light colors.
Use green for Supported, yellow for Partial, and red for Not supported.
Keep color fills distinct from the page background.
Show a color key above the matrix.
Use text labels alongside any rating colors.
Keep Unknown gray or uncolored.
Use yellow for Simulated with an explicit provisional label.
Do not represent missing evidence as an observed middle outcome.
Use a border as an optional secondary marker for the recommended column.
Colors and layout do not establish evidence quality.
