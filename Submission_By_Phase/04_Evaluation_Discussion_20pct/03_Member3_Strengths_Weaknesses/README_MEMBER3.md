# Member 3 - Strengths, Weaknesses, and Limitations

## Main responsibility

Explain what the model does well, what it does not do well, and why the results should be interpreted carefully.

## Files to open

- `Member3_Discussion_Cleaned.md`: recommended presentation version.
Original draft material has been moved to `../../99_Archive_Not_For_Presentation/` for traceability.

## Strengths

- The workflow follows a realistic chronological split instead of random splitting.
- Multiple models were compared: Linear Regression, Ridge Regression, Random Forest, and XGBoost.
- Hyperparameter tuning and time-series cross-validation were used.
- Pipelines reduce preprocessing inconsistency.
- A persistence baseline was included, which makes the evaluation more honest.
- The final test set was only used after model selection.

## Weaknesses

- Directional accuracy is low, so the model is not reliable for predicting up/down movement.
- The persistence baseline slightly outperforms Ridge on 2024 RMSE.
- The project uses only AAPL, so the result may not generalize to other stocks.
- The model does not include news, earnings reports, macroeconomic indicators, or market sentiment.
- Stock markets can change quickly, so historical patterns may not remain stable.

## Short script

The strongest part of our project is the evaluation design. We used chronological splitting, cross-validation, pipelines, and a simple baseline. This reduces data leakage and makes the comparison more realistic. However, the result also has limitations. The model follows the price level well, but directional accuracy is weak, and the persistence baseline slightly beats Ridge on test RMSE. This shows that next-day stock price prediction is difficult and that the model should be interpreted as an academic machine learning workflow, not a real trading system.
