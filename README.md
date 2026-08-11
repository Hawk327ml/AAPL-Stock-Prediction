# AAPL Stock Price Prediction (Group 13)

> **Note on repository name:** This GitHub repo is still named `Traffic-Accident-Data-Analysis` for historical reasons. The actual project is **AAPL next-day adjusted close prediction** (CSM3601 Group 13). Portfolio card: https://hawk327ml.github.io/

## Live demo (Streamlit)

https://aapl-stock-prediction-3scusseltfmnzjcthk2lp8.streamlit.app/

> Streamlit **app source is not yet in this repository** (deployment exists; local web code pending). Notebooks + trained model are included below.

## What is here

Canonical course submission layout under `Submission_By_Phase/`:

| Phase | Content |
|-------|---------|
| `00_Project_Sheet` | Course project sheet |
| `01_Proposal_10pct` | Proposal PDF/DOCX |
| `02_Data_Preparation_EDA_20pct` | Cleaning + EDA notebooks + CSVs |
| `03_Model_Development_30pct` | Model notebook, figures, `models/best_aapl_next_day_model.joblib` |
| `04_Evaluation_Discussion_20pct` | Metrics, graphs, member write-ups |
| `05_Presentation_Demonstration_20pct` | Demo speaking guide + key figures |

Large archives (`.zip` / `.rar`) and draft backups (`99_Archive_*`) are excluded from GitHub.

## Locked result (from model metadata)

- Model: **Ridge Regression** (selected by 2023 validation RMSE before 2024 test)
- 2024 test: MAE **2.1196**, RMSE **2.8764**, R² **0.9873**, directional accuracy **49.00%**
- Target: `Target_Close_t1` (next trading day Adj Close)

## Run notebooks

`ash
pip install -r requirements.txt
`

Start with:

1. `Submission_By_Phase/02_Data_Preparation_EDA_20pct/AAPL_Data_Preparation_EDA_Final.ipynb`
2. `Submission_By_Phase/03_Model_Development_30pct/AAPL_Model_Development.ipynb`
3. `Submission_By_Phase/05_Presentation_Demonstration_20pct/README_PRESENTATION_DEMO.md`

## Poster

See `docs/poster/` (Green Machine Learning web-app poster; metrics on poster may reflect the Streamlit demo variant — CSM3631-style packaging — vs the CSM3601 notebook metrics above).

## Portfolio

https://hawk327ml.github.io/
