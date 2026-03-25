# Case Studies

The handbook should use three applied case studies, one for each core modeling pattern in the course outline.

## 1. Classification case study

Use the Electrical Grid Stability Simulated Data dataset for a binary classification task. The chapter asks the reader to predict whether a power-grid configuration is stable or unstable from the simulated control and load parameters.

- Notebook: `notebooks/05_case_study_classification.ipynb`
- Goal: build a baseline classifier, compare it with a stronger model, and inspect errors with a confusion matrix.
- Main lesson: feature scaling, class balance, and interpretability matter even when the data are synthetic and clean.
- Suggested metrics: accuracy, precision, recall, F1, ROC-AUC.

## 2. Regression case study

Use the Combined Cycle Power Plant dataset for a regression task. The chapter asks the reader to predict net hourly electrical energy output from ambient operating conditions.

- Notebook: `notebooks/06_case_study_regression.ipynb`
- Goal: compare a simple baseline against a better regressor and explain residual patterns.
- Main lesson: regression metrics should be tied to operational meaning, not just leaderboard comparison.
- Suggested metrics: MAE, RMSE, R2.

## 3. Time series case study

Use the Individual Household Electric Power Consumption dataset for a time-aware forecasting task. The chapter asks the reader to predict short-term household power demand after cleaning and resampling the minute-level readings.

- Notebook: `notebooks/07_case_study_time_series.ipynb`
- Goal: build a forecast with lag features, run a time-aware split, and evaluate performance by horizon.
- Main lesson: timestamp parsing, missing-value handling, and leakage prevention are the core skills in time-series work.
- Suggested metrics: MAE, RMSE, sMAPE.

## Chapter Placement

- Chapter 5 should host the classification case study.
- Chapter 6 should host the regression case study.
- Chapter 7 should host the time-series case study.
- Each notebook should mirror the chapter template: data prep, baseline, model comparison, and a short interpretation section.
