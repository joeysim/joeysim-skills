# Experiments

These rules apply when you test or build options to compare them.
An experiment compares options on a shared task.

## Options in an experiment

For each option, also record:

- A hypothesis that explains why the approach could address the problem.
- A falsifier: an observation that would weaken that hypothesis.
- Its build status (built, unbuilt, or unknown), only when the option is something to build.
- A local artifact or preview link for each built variant, when available.
- Its exploration status and supporting evidence.

Use exploration status Observed, Researched, Simulated, Ruled out, or Untested.
Use Researched when cited sources describe the option, but nobody observed it on the shared task.
Use Ruled out only when evidence establishes a constraint violation or weakens the hypothesis enough to reject it.
An unbuilt option can still have useful research or simulation evidence.

## Before an experiment

Save its plan.
If you cannot write files, put the plan in the answer.
Give each part of the plan one line:

- The question and method.
- The baseline and included options.
- The shared task, inputs, and measures.
- Measures that require actual human observations.
- The decision rule, including an inconclusive outcome.
- The resource limit and stopping condition.

Use the same task and measures for comparable tests.
Preserve inspectable variants when implementation affects the result.

## After an experiment

Report every planned measure, including unknown results.
Apply the saved decision rule to the observed evidence.
Classify the result as supports, challenges, or inconclusive.
Update the affected ratings before presenting the revised recommendation.
Link each revision to its predecessor, new evidence, and reason for change.
