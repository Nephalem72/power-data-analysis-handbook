# Notebook Template

Use this as the default structure for instructional notebooks in this handbook. It mirrors the TyumGU analytical-note flow, but removes the decorative and research-team-specific parts.

## Top-Level Order

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

## Suggested Skeleton

```markdown
# Notebook Title
Short subtitle or one-sentence project focus.

## Goal and Expected Outcomes
Describe what the student should learn or produce.

## Task Summary
- What needs to be done
- What data is used
- What final result is expected

## Libraries and Why They Are Used
| Library | Purpose |
| --- | --- |
| pandas | Data loading, cleaning, and aggregation |
| matplotlib / seaborn | Charts and visual analysis |
| scipy / statsmodels | Statistical checks and hypothesis tests |
| sklearn | Modeling and evaluation |

## Data Source and Dataset Notes
- Source:
- Format:
- Time period / scope:
- Known limitations:

## Feature or Column Description
| Feature | Type | Meaning |
| --- | --- | --- |
| ... | ... | ... |

## Analysis Stages
### 1. Data loading and preprocessing
State the stage goal in one or two sentences.

### 2. Exploratory data analysis
State which relationships, anomalies, or patterns are being checked.

### 3. Hypothesis testing or modeling
State the analytical question and evaluation criteria.

### 4. Practical application
Show how the results are used in a course-relevant scenario.

## Code Blocks in Small Steps
One analytical step per code cell. Keep cells short and cohesive.

## Interpretation After Important Outputs
Explain what the table, chart, or metric means for the task.

## Final Conclusions
Summarize the main findings, limits, and next steps.

## Self-Study Questions or Mini Tasks
- Question or exercise 1
- Question or exercise 2

## Sources
Use the citation style required by the course or task.
```

## Fill-In Rules

- Keep the title specific to the notebook topic.
- Make the goal measurable: what should be understood, compared, predicted, or justified.
- Keep the dataset notes factual and brief.
- Use the feature table only for columns that matter to the analysis.
- Expand analysis stages when the task needs more steps, but keep the same narrative order.
- Add self-study questions when the notebook is meant for teaching or revision.

## Preferred Presentation

- Use markdown for structure and explanation.
- Use tables for metadata and summaries.
- Use Styler only for compact summary output.
- Place the interpretation directly below the output it explains.
- Keep console output calm and intentional.
