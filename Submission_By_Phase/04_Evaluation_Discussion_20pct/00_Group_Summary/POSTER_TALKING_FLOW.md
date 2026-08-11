# Poster Talking Flow - Evaluation & Discussion

Use this when speaking from the poster. Keep it simple and avoid turning the presentation into a technical lecture.

## 1. Evaluation design

- Target: next trading day's adjusted close.
- Train: 2015-2022.
- Validation: 2023.
- Test: 2024.
- Model selection was completed before checking the 2024 test set.

Say: chronological splitting is important for time-series data because random splitting can leak future information.

## 2. Metrics

- MAE: average absolute prediction error.
- MSE: squared error, gives stronger penalty to large mistakes.
- RMSE: main selection metric, same unit as stock price.
- R2 Score: how well price-level variation is explained.
- Directional Accuracy: whether predicted up/down movement matches actual movement.

Say: RMSE was selected as the main metric because large price errors matter in regression.

## 3. Final model comparison

- Locked model: Ridge Regression.
- Ridge test RMSE: 2.8764.
- Ridge test R2 Score: 0.9873.
- Ridge directional accuracy: 49.00%.
- Persistence baseline test RMSE: 2.8606.

Say: Ridge was the best trained ML model by validation RMSE, but the persistence baseline slightly beats it on final test RMSE. This is an honest result and shows why simple baselines matter.

## 4. Graphs

- Actual vs predicted prices follow similar overall price levels.
- Residuals show daily prediction errors.
- Larger residuals appear during volatile periods.

Use: `../../05_Presentation_Demonstration_20pct/selected_model_test_predictions_and_residuals.png`.

## 5. Feature importance

- Most important features: Close, Low, Open, MA7, High.
- Recent price-level features dominate next-day close prediction.

Say: this supports the idea that short-term price-level forecasting is highly autocorrelated.

## 6. Strengths and weaknesses

- Strengths: leakage-aware split, pipelines, cross-validation, multiple models, clear baseline.
- Weaknesses: low directional accuracy, one-stock dataset, no news or macro data, limited ability to handle market regime changes.

## 7. Ethics and future work

- Not financial advice.
- High R2 does not mean reliable trading direction.
- Future work: add market index features, simple sentiment indicators, macro indicators, walk-forward retraining, and a clearer dashboard.
