"""Replay AAPL next-day forecast artifacts for portfolio demos.

Default mode prints locked metrics and sample 2024 test rows from saved CSVs.
Optional --rescore loads the joblib pipeline (needs compatible scikit-learn).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PHASE3 = ROOT / "Submission_By_Phase" / "03_Model_Development_30pct"
METADATA = PHASE3 / "models" / "best_model_metadata.json"
TEST_PRED = PHASE3 / "results" / "test_predictions.csv"
MODEL_PATH = PHASE3 / "models" / "best_aapl_next_day_model.joblib"
DATA_PATH = PHASE3 / "data" / "AAPL_Prepared_for_Modeling.csv"


def print_locked_summary() -> dict:
    meta = json.loads(METADATA.read_text(encoding="utf-8"))
    m = meta["test_metrics"]
    print("AAPL Forecast · 次日 Adj Close（Notebook 口径，非交易建议）")
    print("Locked model:", meta["locked_model_name"])
    print("Params:", meta.get("best_parameters"))
    print("Test window:", " → ".join(meta["test_period"]))
    print(
        "Test metrics:"
        f" MAE={m['MAE']:.4f}"
        f" RMSE={m['RMSE']:.4f}"
        f" R2={m['R2']:.4f}"
        f" DirAcc={m['Directional_Accuracy']:.2%}"
    )
    print("Note: not financial advice; directional accuracy is near chance.\n")
    return meta


def print_prediction_samples(n: int = 8) -> None:
    df = pd.read_csv(TEST_PRED)
    cols = [
        "Date",
        "Current_Close",
        "Actual_Target_Close",
        "Persistence_Baseline",
        "Ridge Regression",
    ]
    sample = df.loc[:, cols].tail(n)
    print(f"Last {n} rows from test_predictions.csv:")
    print(sample.to_string(index=False))
    print()


def rescore_last_rows(n: int, meta: dict) -> None:
    import joblib

    package = joblib.load(MODEL_PATH)
    pipeline = package["pipeline"]
    features = package["feature_columns"]
    target = package["target_column"]

    data = pd.read_csv(DATA_PATH, parse_dates=["Date"])
    start, end = pd.Timestamp(meta["test_period"][0]), pd.Timestamp(meta["test_period"][1])
    test = data[(data["Date"] >= start) & (data["Date"] <= end)].copy()
    tail = test.tail(n)

    X = tail[features]
    y = tail[target]
    pred = pipeline.predict(X)

    out = pd.DataFrame(
        {
            "Date": tail["Date"].dt.strftime("%Y-%m-%d"),
            "Actual": y.to_numpy(),
            "Predicted": pred,
            "AbsError": (y.to_numpy() - pred).__abs__(),
        }
    )
    print(f"Rescored last {n} test rows with joblib pipeline:")
    print(out.to_string(index=False))


def main() -> None:
    parser = argparse.ArgumentParser(description="AAPL forecast artifact demo")
    parser.add_argument("--samples", type=int, default=8, help="rows from saved test predictions")
    parser.add_argument(
        "--rescore",
        type=int,
        nargs="?",
        const=5,
        default=None,
        help="re-run joblib pipeline on last N test rows (default 5)",
    )
    args = parser.parse_args()

    meta = print_locked_summary()
    print_prediction_samples(args.samples)
    if args.rescore is not None:
        rescore_last_rows(args.rescore, meta)


if __name__ == "__main__":
    main()
