# Notebook Style Guide

This guide adapts the TyumGU analytical-note template for instructional notebooks in this course. The goal is to keep notebooks readable as teaching material and still practical as executable analysis artifacts.

## Core Principle

Every notebook should tell a clear story:

`goal -> data -> methods -> results -> interpretation -> conclusions -> practice`

Keep the narrative visible in markdown, and keep the code cells small enough that a student can follow the logic without scrolling through a wall of code.

## Recommended Notebook Structure

Use the following section order unless a task clearly requires a different flow:

1. Title
2. Goal and expected outcomes
3. Task summary
4. Libraries and why they are used
5. Data source and dataset notes
6. Feature or column description
7. Analysis stages
8. Code blocks in small steps
9. Interpretation after important outputs
10. Final conclusions
11. Self-study questions or mini tasks
12. Sources

## Markdown Structure

- Use one clear `#` title at the top of the notebook.
- Use `##` for major sections and `###` for subsections.
- Keep headings descriptive and short.
- Place a markdown explanation immediately before a code block when context is needed.
- Place interpretation immediately after the code, chart, or table it explains.
- Use tables for libraries, datasets, feature descriptions, metrics, and comparison summaries.
- Use bullet lists for task steps, assumptions, and conclusions that need to stay concise.

Good markdown rhythm:

`section intro -> code -> result -> interpretation -> next step`

Avoid stacking several code cells in a row without any explanation.

## Output Formatting

Prefer outputs that are easy to scan in class:

- Use plain dataframe output for exploratory inspection.
- Use `pandas.Styler` for compact summary tables, not for every dataframe.
- Use Markdown or HTML blocks for conclusions, callouts, and short structured summaries.
- Keep console output quiet and intentional.
- Format metrics as labeled values or tidy summary tables.
- Put chart interpretation directly below the chart.

When a result matters pedagogically, make it look like a result rather than raw debug output.

### Styler

Use Styler for small, high-value tables such as:

- a compact feature summary;
- a metrics comparison;
- a before/after summary;
- a final ranking table.

Do not use Styler for:

- large raw dataframes;
- intermediate debug tables;
- repetitive formatting on every cell output.

Keep styling restrained:

- highlight only what matters;
- keep number formats consistent;
- avoid heavy gradients and dense color scales unless they explain the result.

### HTML and Markdown Display

Use `IPython.display.display`, `Markdown`, or `HTML` when static table output is not enough.

Good uses:

- short callouts with assumptions or warnings;
- compact multi-line result summaries;
- labeled interpretation blocks;
- visual separation between stages.

Avoid turning notebook prose into decorative web pages. The display layer should clarify the analysis, not distract from it.

## What To Borrow From The TyumGU Template

Borrow these patterns:

- the overall section rhythm: task -> data -> analysis -> interpretation -> conclusions;
- explicit sections for sources and feature descriptions;
- table-based presentation for libraries and dataset metadata;
- a separate interpretation block after key results;
- restrained visual emphasis instead of heavy decoration.

## What To Avoid

Do not copy these parts of the TyumGU template literally:

- decorative symbols in every heading;
- filler wording that does not help the student perform the task;
- team metadata that is not relevant to the course notebook;
- long blocks of text before any code appears;
- large monolithic code cells;
- noisy print dumps and uncontrolled `head()` spam;
- overformatted tables that hide the actual result.

## Code Cell Practice

- Prefer one analytical step per code cell.
- Keep transformations small and named.
- Show the minimum code needed to support the explanation.
- Reuse intermediate variables when the step has teaching value.
- If a calculation is important, show the input, the transformation, and the result close together.

## Writing Results

Write conclusions in plain language:

- state what was found;
- state why it matters;
- state any limitation or caveat;
- connect the result back to the task goal.

For charts and tables, do not rely on the output alone. Add one or two sentences that explain the pattern, surprise, or implication.

## Minimum Quality Check

Before publishing a notebook, confirm that it has:

- a clear title and goal;
- a readable section structure;
- concise code cells;
- interpretation after important outputs;
- formatted summary tables where they add value;
- final conclusions;
- at least one self-study question or follow-up task;
- sources or references where appropriate.
