---
name: decision-matrix
description: Use when a user requests a decision matrix, consequential comparison, scorecard, or trade-off analysis, with or without named options. Also use when a user asks to convert, restyle, export, log, lock, or revisit an existing decision matrix, such as an HTML version of each decision.
metadata:
  version: "1.6.0"
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
Use at most five criteria, unless the user names or asks for more.
Two to four options usually fit one view. Retain more options when the decision requires them.

For each option, record:

- A stable identifier and a title.
- A description, only when a reader cannot tell what the option is from its title. See "Present the matrix".
- A link to its main page, such as its home page, documentation, repository, or model card.

When you test or build options, also record a hypothesis, a falsifier, and a status for each one, as in [the experiment rules](references/experiments.md).
Rule out an option only when evidence shows that it fails a required constraint.
Do not treat an implementation assumption as evidence against an alternative.
Check relevant precedents before claiming novelty.
Keep novelty unknown when no comparison supports the claim.

## Investigate the uncertainty

Use existing evidence when it adequately answers the decision.
Otherwise, choose the smallest comparison that could change the next action.
Research, sketches, a technical check, or one interaction can be sufficient.
Do not build complete products merely to populate the matrix.

An experiment compares options on a shared task. A quote, a call, or a search is a next action, not an experiment.
Before you plan, run, or report an experiment, read [the experiment rules](references/experiments.md).
Explore every listed option before presenting a final comparative recommendation.
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
Use local paths, source links, test records, or identifiable user input as evidence references.
Give each evidence reference an ID: E1, E2, and so on.
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

## Present the matrix

For a personal decision that is easy to reverse, keep the answer short.
Give the recommendation, the criteria with sources, the matrix, what could change the answer, and the evidence.
Leave out option hypotheses, statuses, and the experiment plan unless the user asks for them.

Use Markdown unless the user requests another format or an existing destination requires one.
Place criteria in rows and options in columns.
Keep this orientation across matrices, including narrow layouts.
Number criterion rows 1, 2, 3, and so on.
Label option columns A, B, C, and so on.
Keep these labels consistent within each decision and its supporting explanation.
These labels do not replace stable identifiers.
Place **Recommended** at the top of the recommended option's header, above its letter and title.
Use only **Recommended** or **Selected** as the chip text.
Keep bold text as the fallback for plain Markdown.
Keep the option letter and title in that header.
Keep provisional recommendations explicitly provisional.
Give an option a description only when a reader cannot tell what the option is from its title.
A well-known product, brand, or place needs none, such as `Tesla Model 3` or `Lisbon`.
A label for an approach, or a niche name, needs one, such as `Hybrid` or `Phonon 31M`.
A description says what the option is and how it works, in eight words or fewer.
Put the facts that set options apart, such as a trim or a fuel type, in the cells.
Put it in italic text beneath the title, inside the option header.
Keep each criterion label to four words or fewer, such as `Lease per month`. Give its terms with its source.
Mark required criteria beside their labels.
Leave out a criterion row that every option passes equally, unless the user stated that criterion.
Mention each left-out criterion in one line below the matrix.
Write each rating cell in this order:

1. The color marker, in Markdown only.
2. The key fact, in four words or fewer, as the first sentence: the number or phrase that the criterion asks about, such as `$42,640.` or `IIHS Top Safety Pick.`
3. The basis or the main limit, in one short sentence. Put calculations and other details in `## Evidence`.
4. The evidence IDs, such as E2, E3.

Do not write the rating word, such as Supported or Partial, in the cell. The color shows the rating.
Do not use bold or italic text in rating cells. Give every option the same text style.
For a Simulated rating, start the key fact with "Simulated:".
For an Unknown rating, make the missing evidence the key fact, such as `Not tested.`
When the matrix has scores, add the score to the key fact, such as `0.29 s, score 5.`
Link each tool, framework, model, service, or standard at its first mention.
Link each option title in the matrix header to the option's main page.
Open the option's main page before you link it.
Give only links that you opened or that a cited source gives. Do not guess an address.
Link local files with paths relative to the output file.
Show each rating's color in one way only. The output format sets the way:

| Output | Rating cell | Color key below the matrix |
| --- | --- | --- |
| Plain Markdown | Start the cell with its marker: 🟢 Supported, 🟡 Partial or Simulated, 🔴 Not supported, ⚪ Unknown. | The markers and their labels. |
| Visual, such as HTML | Fill the cell with its background color. | Color swatches and their labels. |

Never combine color markers and background fills.
When you convert Markdown output to HTML, replace each marker with its background fill.

Keep criterion sources, and any option hypotheses you show, close to the table.
When you show statuses, keep exploration status and build status separate from the recommendation label.
State whether the comparison is provisional or complete.
A complete comparison does not prove that every required outcome passed.

Before you make visual output without the bundled script, read [the visual rules](references/visual-output.md).

Say each fact once, in the section that the layout gives it.
Leave out lines that only say that nothing applies, such as no weights or no left-out criteria.
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
For a logged decision, give the decision and the next action in the reply, with links to the decision file and its page. Do not repeat the matrix.
Use the project's existing decisions folder, if it has one. Otherwise, use `docs/decisions/`.

Save each decision in its own file, named `NNN-short-title.md`.
Number the files in order: 001, 002, and so on.
Use this layout for each decision file, in this order:

1. The number and title as a heading, such as `# 001. Speech-out voice`.
2. The date and status, such as `Date: 2026-11-10 · Status: Provisional`.
3. The decision question, in one sentence. The log index shows this sentence as the description.
4. `## Recommendation`, or `## Decision` when the status is Locked: four paragraphs of one sentence each: the recommended or selected option and the main reason, then `Trade-off:`, `Next:`, and `Reconsider:`.
5. `## Matrix`: the matrix, the color key, and the criteria that you left out. Then explain the rating scale and any weights in a `### Rating scale` subsection.
6. `## Criteria`: the intended outcome, the shared task, and each criterion with its source.
7. `## Options`: the baseline and the options that you ruled out. When you test the options, add the hypothesis, falsifier, and status of each.
8. `## Evidence`: the evidence limits, then the checks that you ran and did not run, one line each. When the next action is an experiment, put its plan in a `### Next experiment` subsection.
9. `## References`: one list item for each page that the decision cites or links to. Give its ID, a link with the page's own title as the text, and the publisher, such as `E1. [Lease offers](https://example.com/offers), Example Motors.` Give the read date once above the list, or in each item when the dates differ. Do not write a bare address.
10. `## Revisions`, when the decision has revisions.

When you change a decision file that has another layout, change it to this layout.
Also change its cells and references to the rules in this skill.

Use Provisional, Complete, or Locked as the status.
Set the status to Locked only when the user chooses an option.
Then remove **Recommended**, and put **Selected** at the top of the selected option's header.
Rename `## Recommendation` to `## Decision`.
Add a revision entry with the date, the user's words, and your earlier recommendation.
Change a Locked decision only when the user reopens it.

When new evidence changes a decision, update its file. Do not make a new file.
Add a `## Revisions` section at the end of the file, with the newest revision first.
For each revision, give the date and the new evidence or the user's words. Then give what changed, in three short bullets or fewer.
Preserve earlier decisions and contradictory evidence.
Do not remove compared options merely because they performed poorly.

After each change to the log, run the bundled script. Give the full path of the script and of the decisions folder:

```sh
python3 <skill folder>/scripts/render_html.py <project>/docs/decisions
```

The script writes an HTML page beside each decision file, and an index as `README.md` and `index.html`.
The script gives a note for each file that does not use the layout, the cell order, or reference links.
The pages follow "Present the matrix" and [the visual rules](references/visual-output.md), and link to their Markdown files.
Make all HTML versions of a decision matrix with this script.
Do not edit the files that the script writes.
When the user asks for HTML of a matrix outside the log, add the matrix to the log first.
If the script stops because of a chip, correct the Markdown and run the script again.
For any other stop, give its message to the user and ask how to continue.
