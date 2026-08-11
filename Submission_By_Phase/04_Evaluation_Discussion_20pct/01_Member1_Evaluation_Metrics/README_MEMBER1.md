# Member 1 - Evaluation Metrics

## Main responsibility

Explain how the regression models were evaluated and why Ridge Regression was selected as the locked ML model.

## Files to open

- `Member1_Evaluation_Metrics.ipynb`
- `member1_model_comparison_table.csv`
- `member1_best_model_result.csv`
- `member1_metrics_explanation.md`

## Speaking points

- Our task is regression, so we used MAE, MSE, RMSE, and R2 Score.
- RMSE was the main metric because it penalizes larger prediction errors more strongly and uses the same general scale as stock price.
- Ridge Regression was selected because it had the best validation RMSE among trained ML models.
- On the 2024 test set, Ridge achieved RMSE 2.8764 and R2 Score 0.9873.
- Directional accuracy was 49.00%, so the model should not be used as a trading signal.

## Short script

For evaluation, we used regression metrics because our target is the next trading day's adjusted closing price. RMSE was our main metric because it gives a stronger penalty to large errors. Ridge Regression was selected based on validation performance before looking at the test set. On the final 2024 test set, Ridge achieved RMSE 2.8764 and R2 Score 0.9873, which means it tracks the overall price level well. However, directional accuracy was only about 49%, so the model is useful for academic price-level prediction, not for trading advice.
