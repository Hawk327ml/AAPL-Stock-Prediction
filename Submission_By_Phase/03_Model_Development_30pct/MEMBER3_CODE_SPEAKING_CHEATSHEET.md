# Member 3 Code Speaking Cheatsheet

This file is for Member 3. Use it to explain `AAPL_Model_Development.ipynb` in simple English.

## Your Main Message

Chinese:
我的部分是 model development。前面 Member 2 已经准备好干净的数据和特征，我这里负责把这些特征放进不同的 regression models，使用 time-series cross-validation 和 validation set 选择最稳定的模型，最后只在 test set 上做最终评估。

Simple English:
My part is model development. After data preparation and feature engineering, I train and compare several regression models. I use chronological splitting, pipelines, time-series cross-validation, and hyperparameter tuning. The selected model is Ridge Regression because it has the best validation RMSE among the trained machine learning models.

## 1. Imports, Paths, and Output Folders

Code location: Cell 2

What the code does:
- Imports pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, and joblib.
- Defines `DATA_PATH`, `RESULTS_DIR`, `FIGURES_DIR`, and `MODELS_DIR`.
- Creates output folders automatically.
- Sets `RANDOM_STATE = 42` for reproducible results.

Simple English:
First, I import the libraries and define the file paths. The notebook reads the prepared CSV file and saves result tables, figures, and the final model into separate folders.

If teacher asks "Why random_state = 42?":
It makes the model results reproducible. If we run the notebook again, random-based models such as Random Forest and XGBoost should give the same result.

## 2. Load Data and Check Experimental Design

Code location: Cell 4

Important code:
- `pd.read_csv(DATA_PATH, parse_dates=["Date"])`
- `feature_columns = [...]`
- `target_column = "Target_Close_t1"`
- `train_df`, `validation_df`, `test_df`
- `assert train max date < validation min date < test min date`

What the code does:
- Loads the prepared modeling dataset.
- Defines 18 input features.
- Defines the target as next-day adjusted close.
- Checks required columns, missing values, duplicate dates, and date order.
- Splits the data by the existing `Split` column.

Important numbers:
- Train: 1985 rows, 2015-02-13 to 2022-12-30.
- Validation: 250 rows, 2023-01-03 to 2023-12-29.
- Test: 251 rows, 2024-01-02 to 2024-12-30.
- Features: 18.

Simple English:
Here I load the prepared dataset and define the input features and target. The target is `Target_Close_t1`, which means the adjusted closing price of the next trading day. I also check that the data is sorted by date and that the train, validation, and test periods are strictly chronological.

If teacher asks "Why not random train-test split?":
Because this is time-series stock data. Random splitting may allow future information to leak into training. Chronological splitting is closer to real forecasting.

If teacher asks "What is Target_Close_t1?":
It is tomorrow's adjusted closing price. Features from day t are used to predict the close price on day t+1.

## 3. X and y, Time-Series Cross-Validation

Code location: Cell 6

Important code:
- `X_train = train_df[feature_columns]`
- `y_train = train_df[target_column]`
- `TimeSeriesSplit(n_splits=5, gap=1)`

What the code does:
- Separates features `X` and target `y`.
- Uses expanding-window cross-validation.
- Adds a one-row gap to reduce adjacent target overlap.

Simple English:
In this part, I separate the input features and target variable. Then I use `TimeSeriesSplit`, not normal K-Fold, because the order of time must be respected. Each fold trains on earlier data and validates on later data.

If teacher asks "What does gap=1 mean?":
There is one row between the training part and validation part. It helps reduce leakage because our target is next-day close, so adjacent rows are strongly connected.

If teacher asks "What is cross-validation?":
Cross-validation means training and testing the model several times on different training/validation periods. It gives a more stable estimate than using only one split.

## 4. Pipelines and Models

Code location: Cell 8

Models trained:
- Linear Regression
- Ridge Regression
- Random Forest
- XGBoost

Course-safe explanation:
The main course-aligned models are Linear Regression, Ridge Regression, and Random Forest. XGBoost is included as an extra comparison.

Important code:
- `Pipeline([("scaler", StandardScaler()), ("model", LinearRegression())])`
- `Pipeline([("scaler", StandardScaler()), ("model", Ridge())])`
- `GridSearchCV(...)`

What the code does:
- Uses pipelines so preprocessing and model training happen together.
- Uses `StandardScaler` for Linear Regression and Ridge Regression.
- Uses parameter grids for Ridge, Random Forest, and XGBoost.
- Uses GridSearchCV to find the best hyperparameters by CV RMSE.

Simple English:
I build pipelines for each model. For Linear Regression and Ridge Regression, I use `StandardScaler` because these models are sensitive to feature scale. Then I use `GridSearchCV` to test different hyperparameters and choose the best one based on RMSE.

If teacher asks "Why use Pipeline?":
Pipeline keeps preprocessing and model training together. This avoids inconsistent preprocessing and makes the workflow cleaner and reproducible.

If teacher asks "Why scale only linear models?":
Linear and Ridge Regression depend on coefficient size and feature scale. Tree-based models such as Random Forest do not need scaling in the same way.

If teacher asks "What is alpha in Ridge?":
`alpha` controls the strength of regularization. A larger alpha gives stronger penalty to large coefficients. The best alpha here is 0.01.

## 5. Hyperparameter Tuning Results

Code location: Cell 8 output

Important numbers:
- Ridge Regression Best CV RMSE: 1.6312, best alpha = 0.01.
- Linear Regression Best CV RMSE: 1.6352.
- Random Forest Best CV RMSE: 15.6915.
- XGBoost Best CV RMSE: 15.7619.

Simple English:
After cross-validation, Ridge Regression has the lowest CV RMSE among the trained ML models, slightly better than Linear Regression. Random Forest and XGBoost perform much worse, so they are not selected.

If teacher asks "Why Ridge instead of Linear Regression?":
They are very close, but Ridge has slightly lower validation/CV RMSE and regularization. Regularization helps when features are correlated, which is common in stock price data.

## 6. Validation Comparison and Overfitting Check

Code location: Cell 10

Important code:
- `regression_metrics(...)`
- `Persistence Baseline`
- `Validation_to_Train_RMSE_Ratio > 1.5`
- `locked_model_name = ml_comparison.iloc[0]["Model"]`

What the code does:
- Calculates MAE, MSE, RMSE, R2, and Directional Accuracy.
- Adds persistence baseline: tomorrow's close equals today's close.
- Compares train RMSE and validation RMSE.
- Flags possible overfitting when validation/train RMSE ratio is greater than 1.5.
- Locks Ridge Regression as the selected trained ML model before test evaluation.

Important validation numbers:
- Persistence baseline validation RMSE: 2.1461.
- Ridge validation RMSE: 2.2069.
- Linear validation RMSE: 2.2105.
- XGBoost validation RMSE: 9.2063, overfitting flag true.
- Random Forest validation RMSE: 9.2158, overfitting flag true.

Simple English:
Here I evaluate the models on the 2023 validation set. Ridge Regression is selected as the best trained ML model because it has the lowest validation RMSE among the ML models. I also compare with a persistence baseline. The baseline is slightly better, which shows that stock price-level prediction is difficult and today's close is already a very strong predictor.

If teacher asks "Why select Ridge if persistence baseline is better?":
The project requirement is to train and compare machine learning models. Ridge is the best trained ML model by validation RMSE. The persistence baseline is included as an honest benchmark, and we clearly state that it is very strong.

If teacher asks "What is persistence baseline?":
It is a simple baseline that predicts tomorrow's close price as today's close price. For stock prices, this can be strong because prices are highly autocorrelated.

If teacher asks "Why Random Forest and XGBoost overfit?":
They fit training data better but perform much worse on validation data. Stock prices in 2024/late periods may be outside earlier price ranges, and tree-based models do not extrapolate price levels very well.

## 7. Final Test Evaluation

Code location: Cell 13

Important code:
- `development_df = pd.concat([train_df, validation_df])`
- `clone(search.best_estimator_).fit(X_development, y_development)`
- `prediction = fitted_model.predict(X_test)`
- `test_comparison.to_csv(...)`

What the code does:
- After model selection is locked, it combines train + validation data.
- Re-trains each model using the best hyperparameters.
- Evaluates on the untouched 2024 test set.

Important test numbers:
- Ridge Regression: MAE 2.1196, RMSE 2.8764, R2 0.9873, Directional Accuracy 49.00%.
- Persistence baseline: RMSE 2.8606.
- Linear Regression: RMSE 2.8797.
- Random Forest: RMSE 26.2224.
- XGBoost: RMSE 26.8630.

Simple English:
After choosing the model, I refit the models on train plus validation data and evaluate them on the untouched 2024 test set. Ridge Regression achieves RMSE 2.8764 and R2 0.9873. However, its directional accuracy is only 49%, so it should not be used as a trading signal.

If teacher asks "Why combine train and validation before test?":
After model selection is finished, we can use all available development data to train the final model. The test set is still untouched until final evaluation.

If teacher asks "Does high R2 mean good model?":
Not necessarily. High R2 means it follows the price level well, but directional accuracy is only 49%. So it is not reliable for predicting up or down movement.

## 8. Figures and Feature Importance

Code location: Cells 14 and 16

Figures:
- `validation_comparison_and_overfitting.png`
- `selected_model_test_predictions_and_residuals.png`
- `selected_model_feature_importance.png`

Feature importance method:
- `permutation_importance`
- It shuffles one feature at a time and checks how much RMSE gets worse.

Top features:
- Close
- Low
- Open
- MA7
- High

Simple English:
The prediction graph shows Ridge follows the general price level, but residuals still exist. For feature importance, I use permutation importance. The most important features are recent price-level features such as Close, Low, Open, MA7, and High. This makes sense because next-day close is strongly related to recent prices.

If teacher asks "What is permutation importance?":
It measures how important a feature is by randomly shuffling that feature. If model error increases a lot, the feature is important.

## 9. Save Model and Metadata

Code location: Cell 18

Important code:
- `joblib.dump(model_package, ...)`
- `best_model_metadata.json`
- `model_development_discussion.md`

What the code does:
- Saves the selected model package.
- Saves metadata such as selected model, feature columns, periods, metrics, and library versions.
- Saves a written discussion summary.

Simple English:
Finally, I save the selected model and metadata. This makes the experiment reproducible because we know which model, features, split periods, metrics, and package versions were used.

If teacher asks "Why save metadata?":
Metadata records the experiment setup. It helps others reproduce or check the result later.

## 2-Minute Script For You

Good morning, I am Member 3, and my part is model development.

In this notebook, I use the prepared dataset from the previous phase. First, I define 18 input features and one target variable, `Target_Close_t1`, which means the next trading day's adjusted close price.

Because this is stock time-series data, I do not use random splitting. I use chronological splitting: 2015 to 2022 for training, 2023 for validation and model selection, and 2024 as the final untouched test set.

Then I build pipelines for several regression models: Linear Regression, Ridge Regression, Random Forest, and XGBoost as an extra comparison. I use `GridSearchCV` with `TimeSeriesSplit` to tune hyperparameters. This helps us compare models more fairly while respecting time order.

After validation, Ridge Regression is selected as the best trained machine learning model because it has the lowest validation RMSE among the trained ML models. Random Forest and XGBoost show overfitting because their validation RMSE is much worse than their training RMSE.

Finally, I evaluate the locked model on the 2024 test set. Ridge Regression achieves RMSE 2.8764 and R2 Score 0.9873. However, the persistence baseline is slightly better on RMSE, and directional accuracy is only 49 percent. So our model is useful for demonstrating the machine learning workflow, but it should not be treated as financial advice or a trading system.

## If You Panic, Remember These 5 Sentences

1. My target is next-day adjusted close, `Target_Close_t1`.
2. I use chronological split because random split can cause future-data leakage.
3. I use pipelines and GridSearchCV to tune and compare models fairly.
4. Ridge Regression is selected because it has the best validation RMSE among trained ML models.
5. The model follows price level well, but it is not good enough for trading because directional accuracy is only 49%.

## Most Dangerous Questions and Safe Answers

Q: Why is the baseline better than Ridge?
A: Stock prices are highly autocorrelated, so today's close is already a very strong predictor of tomorrow's close. We include this baseline to make the evaluation honest. Ridge is still the best trained ML model in our comparison.

Q: Why did tree models perform badly?
A: Random Forest and XGBoost can fit training patterns, but they do not naturally extrapolate to new higher price levels. Their validation and test RMSE are much worse, so they show poor generalization.

Q: Why use Ridge Regression?
A: Ridge is similar to Linear Regression but adds regularization. It helps when features are correlated, such as Open, High, Low, Close, and moving averages.

Q: What does RMSE mean?
A: RMSE is the square root of mean squared error. It is in the same unit as the target price, so lower RMSE means smaller prediction error in dollars.

Q: Is this model useful for investment?
A: No. It is an academic machine learning project. The model has high R2 for price level, but directional accuracy is only 49%, so it should not be used as trading advice.

Q: How did you prevent data leakage?
A: We use chronological split, TimeSeriesSplit, a one-row gap, and we do not use the 2024 test set during model selection or tuning.
