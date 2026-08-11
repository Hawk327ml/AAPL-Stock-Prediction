# Evaluation & Discussion - Presentation-Ready Folder

This folder is organized for the project sheet Phase 4 requirement:

- Regression metrics: MAE, MSE, RMSE, R2 Score
- Best-performing model
- Strengths and weaknesses
- Feature importance
- Ethical considerations

## Recommended presentation order

1. `00_Group_Summary/`
   - Use this first. It contains the overall evaluation conclusion and poster/demo speaking flow.

2. `01_Member1_Evaluation_Metrics/`
   - Member 1 explains the evaluation metrics and final model comparison.

3. `02_Member2_Graphs_Feature_Importance/`
   - Member 2 explains actual-vs-predicted graph, residuals, RMSE comparison, and feature importance.

4. `03_Member3_Strengths_Weaknesses/`
   - Member 3 explains model strengths, weaknesses, limitations, and why the persistence baseline matters.

5. `04_Member4_Ethics_Future_Demo/`
   - Member 4 explains ethical considerations, future improvements, demo talking points, and likely Q&A.

Old backups and compressed source files were moved to `../99_Archive_Not_For_Presentation/`. They are kept for traceability but should not be opened during the presentation.

## Key evaluation result

Ridge Regression was selected because it had the lowest 2023 validation RMSE among the trained ML models before the 2024 test set was evaluated.

On the 2024 test set, Ridge Regression achieved:

- MAE: 2.1196
- MSE: 8.2735
- RMSE: 2.8764
- R2 Score: 0.9873
- Directional Accuracy: 49.00%

Important discussion point: the persistence baseline slightly beats Ridge on 2024 RMSE. This should be presented honestly as evidence that next-day stock price-level prediction is difficult and highly autocorrelated.

Presentation advice: keep the explanation simple and course-aligned. The core models to mention are Linear Regression, Ridge Regression, and Random Forest; XGBoost can be described as an extra comparison only if the teacher asks.
