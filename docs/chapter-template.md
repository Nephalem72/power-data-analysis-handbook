# Chapter Template

Use this template for each handbook chapter unless a section is clearly unnecessary.

## 1. Title

Short, specific chapter title that matches the chapter goal.

## 2. Goal and learning outcomes

- State the practical task the chapter solves.
- List 3-5 outcomes that describe what the reader can do after finishing the chapter.
- Mention the case study if the chapter is one of the three applied chapters.

## 3. Theoretical background

Explain the core idea in the context of power data.
Keep the section short and concrete:

- what problem the method solves;
- why the method is appropriate here;
- what can go wrong in practice.

## 4. Key terms

Define the terms the reader must know before using the notebook or doing the lab.

## 5. Short code listings

Show only the minimum code needed to introduce the idea.
Each listing should support one concept and avoid long pipelines.

## 6. Formulas and metrics

Include only the formulas that matter for the chapter.
For each formula, explain:

- the notation;
- how to interpret the result;
- common misuse or leakage risks.

## 7. Mini example

Provide a small, reproducible example tied to the chapter theme.
Use it to connect the theory to the notebook workflow.

## 8. Link to the related notebook

Add a direct link and one sentence on what the notebook contains.

- Notebook: `notebooks/<chapter-number>_<short-name>.ipynb`
- Purpose: show the full workflow, intermediate outputs, and the chapter-specific result.

## 9. Self-check questions

Add 3-5 questions that check understanding of the main concepts, failure modes, and metric interpretation.

## 10. Lab task

Describe one practical assignment that can be completed in the companion notebook or repository.

- Input: dataset, notebook, or chapter artifact to start from.
- Task: the concrete analysis or implementation to perform.
- Output: the expected result, plot, table, metric, or saved file.
- Check: what the reader should verify before considering the task complete.

## 11. Optional recap

Use only if the chapter needs a short closing summary.
Summarize the workflow, the main decision points, and the takeaway for production-style analysis.

