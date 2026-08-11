# Member 4 - Open This File

Use this file as the main path for Member 4. Do not open random files in `04_Evaluation_Discussion_20pct` during the presentation.

## What Member 4 Should Open

1. `MEMBER4_OPEN_THIS.md` - this guide.
2. `Member4_Evaluation_Discussion_Demo.ipynb` - main code/demo notebook.
3. `TEACHER_QA_PREP.md` - if the teacher asks questions.

The notebook loads and displays:

- `test_model_comparison.csv` - final metric table.
- `permutation_feature_importance.csv` - feature importance table.
- prediction/residual and feature-importance figures.

Optional figures are already copied into:

- `../../05_Presentation_Demonstration_20pct/selected_model_test_predictions_and_residuals.png`
- `../../05_Presentation_Demonstration_20pct/selected_model_feature_importance.png`
- `../../05_Presentation_Demonstration_20pct/validation_comparison_and_overfitting.png`

## Simple Speaking Order

1. Open `Member4_Evaluation_Discussion_Demo.ipynb`.
2. Show evaluation metrics: MAE, MSE, RMSE, R2 Score, Directional Accuracy.
3. Show final result: Ridge Regression test RMSE = 2.8764, R2 = 0.9873.
4. Explain honest comparison: persistence baseline RMSE = 2.8606, slightly better than Ridge.
5. Explain interpretation: Ridge follows price level well, but Directional Accuracy is only 49.00%.
6. Show feature importance: Close, Low, Open, MA7, High are most important.
7. End with limitations and ethics: one stock, no news/macro data, not financial advice.

## Short Script

For the evaluation part, we used regression metrics because our target is the next trading day's adjusted closing price. The selected trained ML model is Ridge Regression. On the 2024 test set, Ridge achieved RMSE 2.8764 and R2 Score 0.9873, so it follows the overall price level well.

However, the persistence baseline has a slightly lower RMSE of 2.8606. This means today's close is already a very strong predictor for tomorrow's close. Also, the directional accuracy of Ridge is only 49.00%, so the model should not be used as a trading signal.

For feature importance, the most important features are recent price-level variables such as Close, Low, Open, MA7, and High. This supports the idea that next-day price-level prediction is highly autocorrelated.

Overall, our model is useful for demonstrating the complete machine learning workflow, but it is not financial advice.

## If Teacher Asks Why 04 Looks Like Many Files

Answer:

The folder contains both individual member materials and group summary files. For the actual presentation, we use the cleaned group summary path in `00_Group_Summary`, especially this guide, the final metric table, feature importance table, and Q&A prep.
