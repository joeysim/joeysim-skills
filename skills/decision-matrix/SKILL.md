---
name: decision-matrix
description: Use when a user requests a decision matrix, consequential comparison, scorecard, or trade-off analysis, with or without named options. Also use when a user asks to convert, restyle, export, or revisit an existing decision matrix, such as an HTML version of each decision.
metadata:
  version: "1.2.0"
---

# Decision Matrix

Build a comparison that explains the next useful action and what evidence could change it.
This standalone method requires no specific application, service, or database.

Use this method when alternatives could materially change the result.
For routine choices, give a direct answer unless the user requests a matrix.
Keep generated files in the local workspace.
External publication requires an explicit user request for that destination.

## Start from the available context

The user does not need to supply options, criteria, or an invocation format.
A request such as "Create a decision matrix" is sufficient when the conversation identifies the decision.
Infer the decision question, candidate options, and criteria from the user's goal and available evidence.
State material assumptions explicitly.
If the decision subject is missing or ambiguous, ask one focused question about the goal.
Do not require the user to invent options before proceeding.

When the user names options, compare only those options.
When the named options exclude the current approach, add it as the no-change option.
Mention another credible option in one line outside the matrix when it could change the decision.
When the user names no options, generate credible alternatives.
Keep option generation separate from evidence collection. A generated option has no observed results until evidence supports them.

Apply this method when a consequential comparison helps the current task, even without an explicit skill request.
The agent can use options already under consideration or generate them from context.
Keep autonomous use within the existing task and authority.

Example requests:

- "Create a decision matrix." Use the decision already under discussion.
- "Use $decision-matrix for this goal." Generate suitable options and criteria.
- "Compare option A and option B with $decision-matrix." Use the supplied options.

## Frame the decision

1. State the decision question and the intended outcome.
2. Describe one representative task that all options must address.
3. Identify the current workflow or another justified baseline.
4. Record required capabilities, resource limits, available evidence, and material uncertainty.

Separate the delivery format from the approach to the problem.
For example, a website is a format, while guided steps and direct editing are different approaches.
Use available context before requesting missing information.
Ask about a preference only when its answer materially changes the next action.
Continue authorized, reversible work when an explicit assumption is sufficient.
A comparison request alone does not authorize implementation, spending, or publication.

## Establish shared criteria

Use observable outcomes that distinguish useful options.
Assign each criterion a stable identifier, a clear label, a required flag, and a source.
Express ambiguous criteria as answerable questions.
For example, replace "Speed" with "Can this meet the agreed deadline?"
Define what better means for each criterion, including direction, relevant thresholds, and the comparison baseline.
Use existing limits or evidence for thresholds.
Label any proposed threshold as an assumption.

| Source | Required explanation |
| --- | --- |
| User | An exact quotation and a reference to the original request or later user input. |
| Inference | The reasoning that connects the criterion to the intended outcome. |
| Assumption | The revisable agent choice and its basis. |

Check that each quotation actually supports its criterion.
A matching quotation establishes provenance, not a valid interpretation.
Keep required constraints separate from preferences.
Do not present an inferred preference or implementation choice as a user requirement.
Check whether a criterion unfairly favors one approach before evidence exists.
Preserve required user criteria unless the user authorizes their change or withdraws the underlying direction.
Record reasons for changed inferences or assumptions.

Include material concerns from affected people when the available context identifies them.
Consolidate overlapping criteria without losing distinct requirements.
Record known priorities among optional criteria without inventing weights.
Label inferred priorities as assumptions.

Check whether an option meeting every criterion would justify proceeding.
Investigate remaining objections for missing constraints, unclear criteria, or disputed evidence.
Run this check yourself.
Ask only when unavailable user information materially changes the decision.

## Define credible options

Compare different mechanisms or explanations of the problem.
When only one approach is apparent, consider its opposite or a smaller trial.
Use these prompts only to generate credible alternatives.
Do not invent a compromise or a fixed number of options.
Include the current approach when it remains a credible option.
Otherwise, explain its exclusion or use another justified baseline.
For change decisions, consider a no-change or no-action option, including the benefits forgone by not acting.
Use the current approach for this option when it already represents no change.
Use the fewest options and criteria that cover the decision.
Two to four options and three to six criteria usually fit one view.
Retain additional options or criteria when the decision requires them.

For each option, record:

- A stable identifier, title, and brief description of what the option is and how it works.
- A link to its main page, such as its home page, documentation, repository, or model card.
- A hypothesis that explains why the approach could address the problem.
- A falsifier: an observation that would weaken that hypothesis.
- Its build status (built, unbuilt, or unknown), only when the option is something to build.
- A local artifact or preview link for each built variant, when available.
- Its exploration status and supporting evidence.

Use exploration status Observed, Researched, Simulated, Ruled out, or Untested.
Use Researched when cited sources describe the option, but nobody observed it on the shared task.
Use Ruled out only when evidence establishes a constraint violation or weakens the hypothesis enough to reject it.
An unbuilt option can still have useful research or simulation evidence.
Do not treat an implementation assumption as evidence against an alternative.
Check relevant precedents before claiming novelty.
Keep novelty unknown when no comparison supports the claim.

## Investigate the uncertainty

Use existing evidence when it adequately answers the decision.
Otherwise, choose the smallest comparison that could change the next action.
Research, sketches, a technical check, or one interaction can be sufficient.
Do not build complete products merely to populate the matrix.

Before an experiment, save its plan.
If you cannot write files, put the plan in the answer.
The plan contains:

- The question and method.
- The baseline and included options.
- The shared task, inputs, and measures.
- Measures that require actual human observations.
- The decision rule, including an inconclusive outcome.
- The resource limit and stopping condition.

Explore every listed option before presenting a final comparative recommendation.
Use the same task and measures for comparable tests.
Preserve inspectable variants when implementation affects the result.
Keep the recommendation provisional when an option remains untested or a planned result remains unavailable.
When execution exceeds the request, provide the provisional matrix and the experiment plan.
Do not run that experiment without the necessary authorization.

## Rate every option

Rate every option against every shared criterion exactly once.
Explain the scale directly above or below the matrix.
Use qualitative ratings unless measurements justify numbers.
Define what each applicable rating means for each criterion.
Binary constraints need no artificial middle rating.

| Rating | Meaning |
| --- | --- |
| Supported | Cited evidence supports the criterion within the stated limits. |
| Partial | Cited evidence supports only part of the criterion or includes material limitations. |
| Not supported | Cited evidence shows a failure against the criterion. |
| Unknown | The available evidence does not establish the outcome. |
| Simulated | A model simulation supplies a provisional judgment, not a human observation. |

Adapt these labels when the task needs another clearly defined scale.
Keep Unknown and Simulated explicit.
For each cell, provide the rating, a concise basis, and evidence references for known claims.
Use local paths, source links, test records, or identifiable user input as evidence references.
Record each observation's method, date, and relevant scope.
Explain the missing evidence for Unknown cells.
Do not cite an assumption as proof of an unmeasured outcome.
Separate observations, interpretations, assumptions, and unknowns.
Limit human evidence to the experience actually reported or observed.
Browser checks and model simulations cannot establish human effort, preference, or general usability.

Do not invent weights, measurements, or confidence percentages.
If the user requests numeric scoring, define its anchors, direction, units, and evidence basis.
Keep ordinal judgments distinct from measured quantities.
Use weights only when the user supplies or accepts their meaning.
Do not calculate a total by default.
Never hide a failed required constraint inside an average.
Do not select an option by counting favorable cells.
An unknown required outcome remains unresolved, even when other ratings are favorable.

## Recommend the next action

Start with the recommendation and its main reason.
Use the recommendation and its accepted trade-off as the report or matrix headline.
Choose exactly one recommended option for the current decision.
Specify whether to test, build, or retain that option.
For other decision domains, use an equivalent concrete action.
When evidence cannot support a final choice, recommend one provisional next action.
Use other options as alternatives or test baselines without labeling them Recommended.
State the main trade-off, material unknowns, and the condition for reconsideration.
State which plausible assumptions or preferences could change the recommendation.
Check that numerical trade-offs in the headline and recommendation match the matrix.
Name the baseline, units, and relevant time period for each numerical comparison.
Flag any unexplained differences before presenting those comparisons as established.
Preserve documented disagreement about facts, priorities, or recommendations.
Identify what evidence or user choice could resolve that disagreement.
Do not infer consensus from silence.
Preserve the distinction between the agent's recommendation and the user's actual selection.
Recommendations do not authorize scope changes or override resource limits.

After an experiment, report every planned measure, including unknown results.
Apply the saved decision rule to the observed evidence.
Classify the result as supports, challenges, or inconclusive.
Update the affected ratings before presenting the revised recommendation.
Preserve earlier decisions and contradictory evidence.
Link each revision to its predecessor, new evidence, and reason for change.
Do not remove compared options merely because they performed poorly.

## Present the matrix

For a personal decision that is easy to reverse, keep the answer short.
Give the recommendation, the criteria with sources, the matrix, what could change the answer, and the evidence.
Leave out option hypotheses, statuses, and the experiment plan unless the user asks for them.

Use Markdown unless the user requests another format or an existing destination requires one.
Place criteria in rows and options in columns.
Keep this orientation across matrices, including narrow layouts.
Give option columns equal widths across all visual tables.
Keep those widths stable when descriptions expand or collapse.
Number criterion rows 1, 2, 3, and so on.
Label option columns A, B, C, and so on.
Keep these labels consistent within each decision and its supporting explanation.
These labels do not replace stable identifiers.
Place **Recommended** at the top of the recommended option's header, above its letter and title.
Use a compact, rounded chip for this label in visual output.
Use a neutral or blue chip style that differs from the rating colors.
Use only **Recommended** or **Selected** as the chip text.
For **Selected**, invert the **Recommended** chip: use its text color as the fill, and its fill color as the text.
Keep bold text as the fallback for plain Markdown.
Keep the option letter and title in that header.
State the recommendation action in the explanation above the matrix.
Keep provisional recommendations explicitly provisional.
Place each description inside its option header, beneath the title.
Explain what each option is and how it works in one short sentence.
For visual output, show descriptions expanded by default, with a downward arrow at the left of the sentence.
Put a left border between the arrow and the sentence.
Do not put the arrow on a line of its own.
Collapse the sentence when the user activates the arrow or the sentence.
Show Description beside a right-pointing arrow only when collapsed.
Expand the sentence when the user activates that control.
Use smaller, regular-weight text with readable contrast.
Keep description controls usable with a keyboard and on touch screens.
If collapsible content is unavailable, show the sentence in italic text within the option header.
Mark required criteria beside their labels.
Leave out a criterion row that every option passes equally, unless the user stated that criterion.
Mention each left-out criterion in one line below the matrix.
Place the rating, basis, and evidence reference together in each cell.
Link each tool, framework, model, service, or standard at its first mention.
Link each option title in the matrix header to the option's main page.
Give only links that you opened or that a cited source gives. Do not guess an address.
Link local files with paths relative to the output file.
Show each rating's color in one way only. The output format sets the way:

| Output | Rating cell | Color key above the matrix |
| --- | --- | --- |
| Plain Markdown | Start the rating with its marker: 🟢 Supported, 🟡 Partial or Simulated, 🔴 Not supported, ⚪ Unknown. | The same markers. |
| Visual, such as HTML | Fill the cell with its background color. Start the cell with the rating text. | Color swatches. |

Never combine color markers and background fills.
When you convert Markdown output to HTML, replace each marker with its background fill.

Keep criterion sources, and any option hypotheses you show, close to the table.
When you show statuses, keep exploration status and build status separate from the recommendation label.
State whether the comparison is provisional or complete.
A complete comparison does not prove that every required outcome passed.

For a visual interface, keep descriptions aligned with their option columns.
Show previews only when they represent the compared variants.
Keep text readable at narrow widths.
Use black text on light surfaces and responsive font sizes.
Use clear traffic-light colors in visual output.
Use green for Supported, yellow for Partial, and red for Not supported.
Keep color fills distinct from the page background.
Show a color key above the matrix.
Use text labels alongside any rating colors.
Keep Unknown gray or uncolored.
Use yellow for Simulated with an explicit provisional label.
Do not represent missing evidence as an observed middle outcome.
Use a border as an optional secondary marker for the recommended column.
Colors and layout do not establish evidence quality.

Use one instruction per sentence.
Limit instructions to 20 words and descriptions to 25 words.
Use periods, commas, colons, or parentheses instead of em dashes.
Preserve necessary precision, exact quotations, identifiers, and uncertainty.
Explain any necessary length exception.

Read [the worked example](references/worked-example.md) when distinguishing evidence, simulations, unknowns, or required constraints is difficult.

Before delivery, check criterion coverage, source support, evidence limits, constraint failures, and recommendation consistency.
Check that exactly one option header has a chip: **Recommended**, or **Selected** in a Locked decision.
Check whether new results require revised ratings.
State skipped checks and material risks.

## Keep a decision log

Save each decision matrix that you make in a project folder to the project's decision log.
Keep a decision without a project folder, such as a personal choice, in the answer only.
Use the project's existing decisions folder, if it has one. Otherwise, use `docs/decisions/`.

Save each decision in its own file, named `NNN-short-title.md`.
Number the files in order: 001, 002, and so on.
Use this layout for each decision file, in this order:

1. The number and title as a heading, such as `# 001. Speech-out voice`.
2. The date and status, such as `Date: 2026-11-10 · Status: Provisional`.
3. The decision question, in one sentence. The log index shows this sentence as the description.
4. `## Decision`: start with the recommended or selected option and the main reason. Then give the accepted trade-off, the next action, and what could change the decision.
5. `## Matrix`: the color key, the matrix, and the criteria that you left out. Then explain the rating scale and any weights in a `### Rating scale` subsection.
6. `## Criteria`: the intended outcome, the shared task, and each criterion with its source.
7. `## Options`: the baseline, then each option with its link, description, hypothesis, falsifier, and status. Then the options that you ruled out.
8. `## Evidence`: the evidence limits, and the checks that you ran and did not run.
9. `## References`: each page that the decision links to, with its title, link, and the date that you read it.
10. `## Revisions`, when the decision has revisions.

When you change a decision file that has another layout, change it to this layout.

Use Provisional, Complete, or Locked as the status.
Set the status to Locked only when the user chooses an option.
Then remove **Recommended**, and put **Selected** at the top of the selected option's header.
Add a revision entry with the date, the user's words, and your earlier recommendation.
Change a Locked decision only when the user reopens it.

When new evidence changes a decision, update its file. Do not make a new file.
Add a `## Revisions` section at the end of the file, with the newest revision first.
For each revision, give the date, the new evidence, and what changed.

After each change to the log, run the bundled script. Give the full path of the script and of the decisions folder:

```sh
python3 <skill folder>/scripts/render_html.py <project>/docs/decisions
```

The script writes an HTML page beside each decision file, and an index as `README.md` and `index.html`.
The index shows the description, outcome, status, and date of each decision.
The script gives a note for each file that does not use the layout.
The pages follow the visual rules in "Present the matrix" and link to their Markdown files.
Make all HTML versions of a decision matrix with this script.
Do not edit the files that the script writes.
When the user asks for HTML of a matrix outside the log, add the matrix to the log first.
If the script stops because of a chip, correct the Markdown and run the script again.
For any other stop, give its message to the user and ask how to continue.
