# Evaluation Overview for Presentation

## One-minute summary

Our project predicts the next trading day's adjusted closing price for AAPL. We used chronological evaluation to avoid future-data leakage: 2015-2022 for training, 2023 for validation/model selection, and 2024 as the untouched final test set.

Ridge Regression was selected as the locked ML model because it achieved the lowest validation RMSE among the trained ML models. On the 2024 test set, it achieved RMSE 2.8764 and R2 Score 0.9873, meaning it followed the overall price level well. However, directional accuracy was only 49.00%, so the model should not be treated as a trading signal.

The persistence baseline slightly outperformed Ridge on test RMSE. This is an important and honest finding: for next-day stock price-level prediction, today's price is already a very strong baseline. Our trained model is academically useful for comparing ML workflows, features, and evaluation methods, but it is not reliable for investment decisions.

## Best poster/demo sequence

1. Evaluation setup: chronological split and no test-set tuning.
2. Metric definitions: MAE, MSE, RMSE, R2 Score, directional accuracy.
3. Model comparison table: Ridge selected by validation RMSE; show final 2024 results.
4. Graphs: actual vs predicted, residual plot, RMSE comparison.
5. Feature importance: Close, Low, Open, MA7, High are most important.
6. Strengths and weaknesses: good price-level tracking, weak direction prediction.
7. Ethics and future work: not financial advice; add news/macro features in future.

Presentation caution: do not spend time on advanced early-proposal methods. The final work is easier to defend as a supervised regression workflow using course-aligned models, with XGBoost only as an extra comparison.

## Group speaking roles

- Member 1: Opening introduction and poster overview.
- Member 2: Data preparation, EDA, and feature engineering code.
- Member 3: Model development, model comparison, tuning, and selected model code.
- Member 4: Evaluation metrics, graphs, feature importance, discussion, ethics, and Q&A.
