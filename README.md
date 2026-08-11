# AAPL Stock Price Prediction (Group 13)

> **Note on repository name:** This GitHub repo is still named `Traffic-Accident-Data-Analysis` for historical reasons. The actual project is **AAPL next-day adjusted close prediction** (CSM3601 Group 13). Portfolio: https://hawk327ml.github.io/

## Canonical metrics (notebook / model metadata)

对外展示与 README **以课设 Notebook 锁定结果为准**：

- Model: **Ridge Regression**（先按 2023 validation RMSE 选定，再看 2024 test）
- 2024 test: MAE **2.1196**, RMSE **2.8764**, R² **0.9873**, directional accuracy **49.00%**
- Target: `Target_Close_t1`（下一交易日 Adj Close）

海报（Green ML / Streamlit 包装）上的数字可能不同，**不作对外权威指标**。

## Live demo & poster (no app source)

- **Live (Streamlit Cloud):** https://aapl-stock-prediction-3scusseltfmnzjcthk2lp8.streamlit.app/
- **Poster:** `docs/poster/AAPL_Green_ML_Poster.png`

原 Streamlit 网页源码已不可得，本仓库**不收录、不重建** web 源码；作品集仅保留 Live 链接 + 海报 + Notebook 课设材料。

## What is here

Canonical course submission under `Submission_By_Phase/`:

| Phase | Content |
|-------|---------|
| `00_Project_Sheet` | Course project sheet |
| `01_Proposal_10pct` | Proposal PDF/DOCX |
| `02_Data_Preparation_EDA_20pct` | Cleaning + EDA notebooks + CSVs |
| `03_Model_Development_30pct` | Model notebook, figures, `models/best_aapl_next_day_model.joblib` |
| `04_Evaluation_Discussion_20pct` | Metrics, graphs, member write-ups |
| `05_Presentation_Demonstration_20pct` | Demo speaking guide + key figures |

Large archives (`.zip` / `.rar`) and draft backups (`99_Archive_*`) are excluded from GitHub.

## Run notebooks

```bash
pip install -r requirements.txt
```

Start with:

1. `Submission_By_Phase/02_Data_Preparation_EDA_20pct/AAPL_Data_Preparation_EDA_Final.ipynb`
2. `Submission_By_Phase/03_Model_Development_30pct/AAPL_Model_Development.ipynb`
3. `Submission_By_Phase/05_Presentation_Demonstration_20pct/README_PRESENTATION_DEMO.md`

## Portfolio

https://hawk327ml.github.io/
