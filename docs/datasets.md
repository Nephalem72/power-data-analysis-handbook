# Dataset Candidates

These datasets are the recommended teaching set for the three applied chapters. They are public, stable, and small enough to document clearly while still showing real preprocessing decisions.

| Task type | Dataset | Source URL | File format | Scale | Target | Key features | Preprocessing issues | Notebook placement | Acquisition note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Classification | Electrical Grid Stability Simulated Data | https://archive.ics.uci.edu/dataset/471/electrical+grid+stability+simulated+data | CSV | 10,000 rows x 12 columns | `stabf` (stable / unstable) | `tau1`-`tau4`, `p2`-`p4`, `g1`-`g4`; `p1` is non-predictive and can be dropped for a cleaner feature set | No missing values; check class balance; standardize features for linear models; keep the simulated nature explicit in the chapter narrative | `notebooks/05_case_study_classification.ipynb` | Download from UCI or fetch with `ucimlrepo` (`id=471`) |
| Regression | Combined Cycle Power Plant | https://archive.ics.uci.edu/dataset/294/combined+cycle+power+plant | XLSX and ODS | 9,568 rows x 5 columns | `PE` (net hourly electrical energy output) | Ambient `AT`, `V`, `AP`, `RH` measured from plant sensors | No missing values; features are on different scales; do not treat the shuffled UCI files as a time series; use a train/test split that preserves teaching clarity | `notebooks/06_case_study_regression.ipynb` | Download from UCI or fetch with `ucimlrepo` (`id=294`) |
| Time series | Individual Household Electric Power Consumption | https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption | Semicolon-delimited text (`.txt`) | 2,075,259 rows x 9 columns | `Global_active_power` for forecasting or resampled load aggregates | `Date`, `Time`, `Voltage`, `Global_reactive_power`, `Global_intensity`, `Sub_metering_1`-`3` | Parse and combine date/time; handle missing values encoded as empty fields; resample to a manageable frequency; the raw file is large, so teach on a window or sampled period | `notebooks/07_case_study_time_series.ipynb` | Download from UCI or fetch with `ucimlrepo` (`id=235`) |

## Selection Notes

- The classification and regression datasets are fully tabular and low-friction for first-pass modeling.
- The time-series dataset is intentionally larger so the handbook can demonstrate parsing, resampling, lag features, and backtesting.
- All three sources have clear documentation and CC BY 4.0 licensing on UCI, which makes them easy to cite in teaching material.
