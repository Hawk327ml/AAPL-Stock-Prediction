# Project Check Checklist

## What is ready

- All three main notebooks are executed from top to bottom with no stored error outputs.
- Cleaned data and modeling data have no missing values or duplicate rows.
- The modeling dataset in the root folder is byte-for-byte identical to `Model_Development/data/AAPL_Prepared_for_Modeling.csv`.
- Model selection uses the 2023 validation set before evaluating the untouched 2024 test set.
- Result tables, figures, saved model, and metadata are present in `Model_Development/`.
- Evaluation discussion files are present in `Evaluation_Discussion/Member1_Evaluation_Metrics/`.

## Points to mention if asked

- Ridge Regression was locked because it had the lowest validation RMSE among the trained ML models.
- The persistence baseline slightly outperforms Ridge on 2024 test RMSE, which is common for next-day stock price-level prediction.
- Directional accuracy is limited, so the model should not be presented as a trading signal or financial advice.
- `Legacy_Previous_EDA/` is retained only as historical work and is not used by the final workflow.

## Suggested teacher review path

1. Read `README.md`.
2. Open `AAPL_Data_Preparation_EDA_Final.ipynb` for final EDA and feature engineering.
3. Open `Model_Development/AAPL_Model_Development.ipynb` for model training, tuning, and evaluation.
4. Review `Model_Development/results/model_development_discussion.md` and `Evaluation_Discussion/Member1_Evaluation_Metrics/member1_metrics_explanation.md`.
