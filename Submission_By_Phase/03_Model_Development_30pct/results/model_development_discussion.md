# Model Development Discussion

## Selection
The model was selected using 2023 validation RMSE before the 2024 test set was evaluated. The locked model is **Ridge Regression**.

## Final test performance
- MAE: 2.1196
- MSE: 8.2735
- RMSE: 2.8764
- R-squared: 0.9873
- Directional Accuracy: 49.00%

The locked model did not outperform the persistence baseline on test RMSE. Potential overfitting flag: **False**.

## Overfitting and model behavior
Models flagged by a validation-to-training RMSE ratio above 1.5: **XGBoost, Random Forest**. Random Forest and XGBoost are strong nonlinear learners, but tree ensembles do not naturally extrapolate beyond the price levels observed during fitting. Their generalization gaps are therefore important evidence when the market enters a higher-price regime. The regularized Ridge model was selected because its validation performance was more stable, not because of training fit alone.

## Strengths
- Chronological evaluation mirrors real forecasting.
- Pipelines prevent preprocessing inconsistency.
- Expanding-window cross-validation and a one-row gap reduce temporal leakage.
- The untouched test set is evaluated only after model selection.

## Weaknesses
- Daily stock movements have low signal-to-noise ratio and may change across market regimes.
- Strongly correlated price features can divide permutation importance across related variables.
- High price-level R-squared can coexist with limited directional accuracy, so the persistence baseline is essential.
- Results cover one stock and one historical period and should not be treated as investment advice.

## Ethical considerations
Predictions are uncertain and may encourage financial risk if presented without limitations. The model excludes news, macroeconomic events, transaction costs, and sudden structural changes. Outputs are for academic analysis, not financial advice.
