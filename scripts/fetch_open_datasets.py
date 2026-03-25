from __future__ import annotations

from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw" / "external"
SAMPLE_DIR = ROOT / "data" / "sample"


def ensure_dirs() -> None:
    for path in [
        RAW_DIR,
        SAMPLE_DIR / "classification",
        SAMPLE_DIR / "regression",
        SAMPLE_DIR / "time_series",
    ]:
        path.mkdir(parents=True, exist_ok=True)


def fetch_classification() -> None:
    dataset = fetch_ucirepo(id=471)
    frame = pd.concat([dataset.data.features, dataset.data.targets], axis=1)
    frame.to_csv(RAW_DIR / "electrical_grid_stability_full.csv", index=False)
    frame.to_csv(
        SAMPLE_DIR / "classification" / "electrical_grid_stability.csv", index=False
    )


def fetch_regression() -> None:
    dataset = fetch_ucirepo(id=294)
    frame = pd.concat([dataset.data.features, dataset.data.targets], axis=1)
    frame.to_csv(RAW_DIR / "combined_cycle_power_plant_full.csv", index=False)
    frame.to_csv(
        SAMPLE_DIR / "regression" / "combined_cycle_power_plant.csv", index=False
    )


def fetch_time_series() -> None:
    dataset = fetch_ucirepo(id=235)
    raw = dataset.data.original.copy()
    raw["timestamp"] = pd.to_datetime(
        raw["Date"] + " " + raw["Time"],
        format="%d/%m/%Y %H:%M:%S",
        errors="coerce",
    )

    numeric_cols = [
        "Global_active_power",
        "Global_reactive_power",
        "Voltage",
        "Global_intensity",
        "Sub_metering_1",
        "Sub_metering_2",
        "Sub_metering_3",
    ]
    for column in numeric_cols:
        raw[column] = pd.to_numeric(raw[column], errors="coerce")

    clean = raw.dropna(subset=["timestamp"]).copy()
    clean.to_csv(
        RAW_DIR / "household_power_consumption_full.csv.gz",
        index=False,
        compression="gzip",
    )

    january = clean.loc[
        (clean["timestamp"] >= "2007-01-01") & (clean["timestamp"] < "2007-02-01")
    ].copy()
    hourly = (
        january.set_index("timestamp")[numeric_cols]
        .resample("h")
        .mean()
        .reset_index()
    )
    hourly["hour"] = hourly["timestamp"].dt.hour
    hourly["day_of_week"] = hourly["timestamp"].dt.dayofweek
    hourly["load_lag_1"] = hourly["Global_active_power"].shift(1)
    hourly["load_roll_3"] = hourly["Global_active_power"].rolling(window=3).mean()
    hourly.to_csv(
        SAMPLE_DIR / "time_series" / "household_power_hourly_january_2007.csv",
        index=False,
    )


def main() -> None:
    ensure_dirs()
    fetch_classification()
    fetch_regression()
    fetch_time_series()
    print("Datasets fetched and samples prepared.")


if __name__ == "__main__":
    main()
