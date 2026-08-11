# Group 13 Presentation and Demo Guide

Use this as the main opening file for tomorrow. The instructor has confirmed that slides are not required, and the main focus is code plus how the workflow runs.

## Main message

We built a supervised regression workflow to predict the next trading day's adjusted closing price for AAPL. The project covers data cleaning, EDA, feature engineering, model comparison, evaluation, interpretation, and responsible limitations.

## Member speaking flow

1. Member 1: opening introduction and poster overview.
2. Member 2: `02_Data_Preparation_EDA_20pct` - data cleaning, EDA, feature engineering, and modeling CSV output.
3. Member 3: `03_Model_Development_30pct` - train/validation/test split, model pipelines, cross-validation, hyperparameter tuning, and selected model.
4. Member 4: `04_Evaluation_Discussion_20pct` - metrics, graphs, feature importance, strengths/weaknesses, ethics, and Q&A.

## Core story

1. Problem background: AAPL next-day closing price prediction.
2. Data preparation: 2015-2024 adjusted OHLCV data, no missing values, chronological order.
3. Feature engineering: moving averages, daily returns, volatility, price range, lagged close/return features.
4. Model development: Linear Regression, Ridge Regression, Random Forest, plus XGBoost as an extra comparison.
5. Evaluation design: train 2015-2022, validation 2023, final test 2024.
6. Key result: Ridge Regression was selected by validation RMSE before checking the 2024 test set.
7. Honest interpretation: Ridge test RMSE is 2.8764 and R2 is 0.9873, but the persistence baseline is slightly better on RMSE and directional accuracy is only 49.00%.
8. Conclusion: the workflow is academically strong, but the model is not financial advice or a trading signal.

## Files to open if needed

- Opening guide: `README_PRESENTATION_DEMO.md`
- Member 2 main notebook: `../02_Data_Preparation_EDA_20pct/AAPL_Data_Preparation_EDA_Final.ipynb`
- Member 3 main notebook: `../03_Model_Development_30pct/AAPL_Model_Development.ipynb`
- Member 4 guide: `../04_Evaluation_Discussion_20pct/00_Group_Summary/MEMBER4_OPEN_THIS.md`
- Member 4 main notebook: `../04_Evaluation_Discussion_20pct/00_Group_Summary/Member4_Evaluation_Discussion_Demo.ipynb`
- Evaluation summary: `../04_Evaluation_Discussion_20pct/00_Group_Summary/EVALUATION_OVERVIEW_FOR_PRESENTATION.md`
- Q&A prep: `../04_Evaluation_Discussion_20pct/00_Group_Summary/TEACHER_QA_PREP.md`
- Actual vs predicted/residual figure: `selected_model_test_predictions_and_residuals.png`
- Feature importance figure: `selected_model_feature_importance.png`
- Validation comparison figure: `validation_comparison_and_overfitting.png`

## Avoid during presentation

- Do not overclaim that the model is good for trading.
- Do not spend time explaining advanced early-proposal methods unless the teacher asks.
- Do not open files from `../99_Archive_Not_For_Presentation/` during the presentation.
- Do not say Ridge beats every baseline; say it was the best trained ML model by validation RMSE, while persistence remains a very strong baseline.
