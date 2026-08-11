# Member 2 - Graphs and Feature Importance

## Main responsibility

Explain the evaluation graphs and feature importance results.

## Files to open

- `actual_vs_predicted.png`
- `residual_plot.png`
- `rmse_comparison_graph.png`
- `feature_importance_graph.png`
- `test_model_comparison.csv`
- `permutation_feature_importance.csv`

## Speaking points

- The actual-vs-predicted graph shows that Ridge Regression follows the general 2024 AAPL price trend.
- The residual plot shows where the model overpredicts or underpredicts.
- The RMSE comparison graph shows Ridge and Linear Regression are close, while tree-based models generalize poorly on 2024 data.
- Feature importance shows Close, Low, Open, MA7, and High are the top contributors.
- This makes sense because next-day stock close is strongly related to recent price levels.

## Short script

The graphs help us interpret the model beyond the table of metrics. The actual-vs-predicted plot shows that the selected model follows the overall price level, but the residual plot reminds us that daily errors still exist. The RMSE comparison shows that simple linear models perform much better than Random Forest and XGBoost on the 2024 test set. From permutation feature importance, the most important variables are recent price-level features such as Close, Low, Open, MA7, and High.
