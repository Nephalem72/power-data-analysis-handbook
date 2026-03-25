# Handbook Outline

Course focus: practical power data analysis with a reproducible workflow, one companion notebook per chapter, and three applied case studies.

## Chapter Map

1. **Course setup and workflow**
   - Goal: explain the handbook structure, repository layout, notebook conventions, and reproducibility expectations.
   - Notebook link: `notebooks/01_course_setup.ipynb`
   - Practice: verify the local environment, run the first notebook, and inspect the saved outputs.

2. **Power data, sources, and quality**
   - Goal: describe common data sources, table structure, missingness patterns, leakage risks, and basic validation checks.
   - Notebook link: `notebooks/02_data_sources_and_quality.ipynb`
   - Practice: profile a raw dataset and document issues that must be fixed before modeling.

3. **Exploratory analysis and feature design**
   - Goal: turn raw measurements into interpretable summaries, time-aware aggregates, and candidate predictors.
   - Notebook link: `notebooks/03_eda_and_features.ipynb`
   - Practice: build a short EDA report and compare at least two feature sets.

4. **Splitting, metrics, and model selection**
   - Goal: establish train/validation/test discipline, choose metrics, and avoid common evaluation mistakes.
   - Notebook link: `notebooks/04_splitting_metrics_and_baselines.ipynb`
   - Practice: create a baseline, compare metrics, and justify the chosen evaluation scheme.

5. **Case study 1: classification**
   - Goal: solve a classification task on power-domain data, from preprocessing through interpretation.
   - Notebook link: `notebooks/05_case_study_classification.ipynb`
   - Practice: train a classifier, inspect confusion-matrix errors, and explain the main failure modes.

6. **Case study 2: regression**
   - Goal: solve a regression task and connect error metrics to operational meaning.
   - Notebook link: `notebooks/06_case_study_regression.ipynb`
   - Practice: compare a baseline and a stronger regressor, then interpret residual patterns.

7. **Case study 3: time series**
   - Goal: handle temporal ordering, lag features, forecasting horizons, and backtesting.
   - Notebook link: `notebooks/07_case_study_time_series.ipynb`
   - Practice: build a forecast, run a time-aware split, and assess error by horizon.

8. **Interpretation, uncertainty, and reporting**
   - Goal: explain model behavior, quantify uncertainty where relevant, and write results for a technical audience.
   - Notebook link: `notebooks/08_interpretation_and_reporting.ipynb`
   - Practice: produce a compact results summary with assumptions, limitations, and next steps.

9. **Capstone integration**
   - Goal: combine the workflow into a small end-to-end project and prepare a final deliverable.
   - Notebook link: `notebooks/09_capstone.ipynb`
   - Practice: complete an integrated analysis that reuses the same reproducible structure from the earlier chapters.

## Design Principles

- Every chapter should pair theory with one notebook that demonstrates the same workflow on a concrete power-data task.
- The three case studies should be distinct: one classification problem, one regression problem, and one time series problem.
- Each chapter should end with self-check questions and a lab task that can be completed with the companion notebook or the repository data.
- Keep the handbook focused on engineering decisions: inputs, transformations, metrics, outputs, and saved artifacts.
- Favor short, reusable examples over long code blocks.

