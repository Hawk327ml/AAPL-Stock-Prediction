# Project Check Checklist

## What is ready

- Main notebooks under `Submission_By_Phase/` run top-to-bottom without stored error outputs.
- Cleaned / modeling CSVs have no missing values or duplicate rows.
- Modeling CSV in phase 02 matches `03_Model_Development_30pct/data/AAPL_Prepared_for_Modeling.csv`.
- Model selection uses the 2023 validation set before the untouched 2024 test set.
- Result tables, figures, saved model, and metadata live under `03_Model_Development_30pct/`.
- Evaluation discussion files live under `04_Evaluation_Discussion_20pct/`.

## Points to mention if asked

- Ridge was locked for lowest **validation** RMSE among trained ML models (not because of test peeking).
- Persistence baseline can slightly beat Ridge on 2024 test RMSE — common for next-day price-level tasks.
- Directional accuracy ≈ 49%, so do **not** pitch this as a trading signal.
- Canonical public metrics: MAE 2.12 / RMSE 2.88 / R² 0.987 (notebook / `best_model_metadata.json`).

## Suggested review path

1. Read root `README.md`.
2. Open `02_Data_Preparation_EDA_20pct/AAPL_Data_Preparation_EDA_Final.ipynb`.
3. Open `03_Model_Development_30pct/AAPL_Model_Development.ipynb`.
4. Skim `03_Model_Development_30pct/results/model_development_discussion.md`.
5. Optional demo: `python scripts/predict_demo.py`.
