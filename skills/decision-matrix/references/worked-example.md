# Worked example

This example is fictional. Its evidence labels represent supplied records, not sources to cite in real decisions.
Real matrices must link to actual evidence.
This example shows the reasoning, not the layout of a decision file.

## Supplied request and evidence

User request U1: "The tool must run offline and cost no more than $5 per month. I want fewer corrections."

The user supplied no options. The agent proposed alternatives from the goal and current workflow before collecting the evidence below.

- E1: A browser test completed the editing task offline in the current form. Its recorded monthly cost is $0.
- E2: A browser test completed the same task offline in a guided prototype. Its recorded monthly cost is $2.
- E3: A model simulation predicted fewer corrections with the guided prototype. No person tested that prediction.
- E4: The hosted assistant requires a network connection and costs $8 per month under the supplied terms.

## Recommend testing B: delay adoption to check the predicted benefit

Test the guided prototype (B) against the current form (A) with people before adopting it.
B meets the recorded technical and cost constraints and has a predicted benefit worth testing. E2–E3.
Use A as the comparison baseline.
The hosted assistant fails both required constraints.
The guided prototype has functional evidence, but its predicted human benefit remains provisional.

Decision question: Which approach merits the next test?
Shared task: Correct one erroneous value in the same sample record.
Baseline: The current form.
Trade-off: B may reduce corrections but costs $2 more per month than A. E1–E3.
Comparison status: Provisional for human outcomes.

## Criteria and sources

| No. | ID | Criterion question | Required | Source |
| --- | --- | --- | --- | --- |
| 1 | offline | Can the task finish without a network connection? | Yes | User, U1: "The tool must run offline". |
| 2 | cost | Does monthly cost stay at or below $5? | Yes | User, U1: "cost no more than $5 per month". |
| 3 | corrections | Does this require fewer corrections than the current form? | No | Inference from U1: "I want fewer corrections." The baseline defines the comparison. |

Rating definitions:

- Offline: Supported requires completion without a network connection. A required network connection means Not supported.
- Cost: Supported means at most $5 per month. A cost above $5 means Not supported.
- Corrections: Supported requires fewer human correction attempts without reducing successful completion. This comparison rule is an assumption.
- Equal or greater correction attempts mean Not supported for improvement. Conflicting human results can justify Partial with an explanation.
- Missing human observations mean Unknown. A model prediction remains Simulated.

Priority: The required constraints apply before the preference for fewer corrections.
The user supplied no preference between cheaper options that satisfy the monthly limit.
The agent must not invent that preference or agreement among stakeholders.

Sufficiency check: Meeting the constraints and reducing corrections supports proceeding only if people can still complete the task.
The comparison rule includes successful completion. Human evidence for that outcome remains missing.

Assumption: The sample editing task represents the work that needs improvement.
This assumption remains revisable. It does not create a new user requirement.

## Options

Option A keeps the current workflow unchanged.

| Detail | A. Current form | B. Guided prototype | C. Hosted assistant |
| --- | --- | --- | --- |
| Description | Edit values directly in the existing form. | Follow guided prompts to correct one value at a time. | Ask an online assistant to correct a value. |
| Hypothesis | Direct access limits unnecessary interaction. | Sequential prompts reduce correction errors. | Natural language helps people identify the intended correction. |
| What would weaken it? | People repeatedly correct the wrong field. | People make as many corrections as with the current form. | People repeatedly correct the assistant's interpretation. |
| Build and exploration status | Built. Observed technical behavior, E1. | Built. Observed technical behavior, E2. Simulated human benefit, E3. | Unbuilt locally. Ruled out by documented constraints, E4. |

## Matrix

Scale: Supported means evidence meets the criterion. Not supported means evidence shows a failure.
Unknown means the outcome lacks evidence. Simulated means a model supplied the judgment.

Color key: 🟢 Supported. 🟡 Partial or Simulated. 🔴 Not supported. ⚪ Unknown.

| Criterion | A. Current form *Edit values directly in the existing form.* | **Recommended** B. Guided prototype *Follow guided prompts to correct one value at a time.* | C. Hosted assistant *Ask an online assistant to correct a value.* |
| --- | --- | --- | --- |
| 1. Offline task (Required) | 🟢 Works offline. The browser completed the task offline. E1. | 🟢 Works offline. The browser completed the same task offline. E2. | 🔴 Needs a network. The service requires a network connection. E4. |
| 2. Monthly cost (Required) | 🟢 $0 per month. E1. | 🟢 $2 per month. E2. | 🔴 $8 per month. Over the $5 limit. E4. |
| 3. Fewer corrections | ⚪ No human baseline. Nobody measured corrections in the current form. | 🟡 Simulated: fewer corrections. A model predicted it, but no person tested it. E3. | ⚪ Not tested. No person tested this option. |

There is no total score.
A favorable prediction cannot compensate for a failed required constraint.
Exploration evidence for an option does not establish every outcome for that option.

## Next experiment

Question: Does the guided prototype reduce correction errors on the representative task?
Method: Compare both local variants with people using the same task and equivalent records.
Baseline: The current form.
Measures: Additional correction attempts, successful completion, and failures against required constraints.
Human measures: Correction attempts and successful completion by people.
Decision rule: Prefer the guided prototype if it reduces corrections without reducing successful completion or violating either required constraint.
Otherwise, retain the current form or classify conflicting results as inconclusive.
Stopping condition: Stop at the agreed session limit or when a required constraint fails.
Resource boundary: Participant access and the session limit remain unspecified. This example authorizes no recruitment or spending.

Reconsideration condition: Relevant human observations contradict the prediction or either option fails a required constraint.
A later decision must retain this record and explain any changed recommendation.

Skipped checks: No human sessions or production cost checks occurred in this fictional example.
Risk: Simulated improvement may not transfer to actual use.
