# Teacher Q&A Prep

## Why did you choose Ridge Regression?

Ridge Regression had the lowest validation RMSE among the trained ML models. We selected it before evaluating the 2024 test set, so the test set remained untouched for final evaluation.

## Why does the persistence baseline slightly beat Ridge on test RMSE?

Stock prices are highly autocorrelated. For next-day price-level prediction, today's close is already a strong predictor of tomorrow's close. The baseline result shows why comparing against a simple baseline is necessary.

## Does high R2 mean the model is good for trading?

No. High R2 means the model follows the overall price level, but directional accuracy is only about 49%. That is not reliable enough for trading decisions.

## How did you prevent overfitting?

We used chronological train/validation/test splits, TimeSeriesSplit cross-validation with a one-row gap, pipelines, hyperparameter tuning only on training/validation data, and final test evaluation only after model selection.

## What are the most important features?

Permutation importance shows that Close, Low, Open, MA7, and High are the strongest features. These are recent price-level indicators, which is expected for next-day close prediction.

## What would you improve?

We would add market index features, simple news or sentiment indicators, macroeconomic indicators, walk-forward retraining, and a clearer dashboard for demonstration.

## The proposal mentioned LSTM, GRU, and ARIMA. Why are they not the main final models?

They were early candidate ideas. For the final project, we focused on the supervised regression workflow required by the course: preprocessing, feature engineering, train-validation-test split, pipelines, cross-validation, model comparison, and regression metrics. This made the project easier to explain and evaluate fairly within the course scope.
