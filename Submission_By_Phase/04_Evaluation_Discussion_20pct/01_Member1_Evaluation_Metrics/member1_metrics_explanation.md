# Member 1 Evaluation Metrics Explanation

Based on the evaluation results, **Ridge Regression** was selected as the best machine learning model because it achieved the lowest validation RMSE among the trained ML models and remained stable on the unseen 2024 test set. RMSE was used as the main metric because it gives a higher penalty to large prediction errors, which is important in stock price prediction.

On the test set, Ridge Regression achieved:

- MAE: 2.1196
- MSE: 8.2735
- RMSE: 2.8764
- R2 Score: 0.9873
- Directional Accuracy: 0.4900

The high R2 Score shows that the model followed the overall AAPL price level well. However, Directional Accuracy was not high, so the model should not be used as a reliable trading signal or financial advice. It is mainly suitable for academic learning and price-level prediction.
