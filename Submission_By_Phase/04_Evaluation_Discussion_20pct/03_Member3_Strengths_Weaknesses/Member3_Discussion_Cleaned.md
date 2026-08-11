# Member 3 Discussion - Cleaned Version

## Best-Performing Model Discussion

Among all the machine learning models evaluated, **Ridge Regression** was selected as the best-performing machine learning model. It achieved the lowest validation RMSE among the trained ML models while maintaining a good balance between prediction accuracy and generalization ability. Compared with Random Forest and XGBoost, Ridge Regression produced more consistent results on unseen data.

The regularization mechanism in Ridge Regression helps reduce model complexity by preventing excessively large coefficients. This is useful because many stock-price features are highly correlated. Therefore, Ridge Regression was considered the most suitable trained model for predicting the next-day adjusted closing price of AAPL in this project.

## Overfitting Discussion

The experimental results indicate that **Random Forest** and **XGBoost** showed signs of overfitting. These models performed relatively well during training but performed much worse on validation and test data. This suggests that they learned patterns specific to the training period rather than general market behavior.

In contrast, Ridge Regression showed more stable generalization. Its performance gap was smaller, and it avoided the severe validation-to-test degradation shown by the tree-based models.

## Strengths of the Model

- A chronological train-validation-test split was used, which prevents future-data leakage and better reflects real-world stock prediction.
- Multiple machine learning models were compared.
- Regression metrics including MAE, MSE, RMSE, R2 Score, and Directional Accuracy were used.
- Feature importance analysis improved interpretability.
- Cross-validation and pipelines improved robustness and reduced preprocessing inconsistency.
- A persistence baseline was included for a fair comparison.

## Weaknesses and Limitations

- The prediction model mainly uses historical price and volume data.
- External factors such as financial news, market sentiment, macroeconomic indicators, interest rates, and company announcements were not included.
- A high R2 Score does not guarantee strong trading performance because stock prices are naturally continuous and highly autocorrelated.
- Directional Accuracy remained limited, so the model is weak for predicting up/down movement.
- The model was evaluated only on AAPL, so the findings may not generalize to other stocks or markets.
- The persistence baseline slightly outperformed Ridge on 2024 test RMSE, showing that next-day price-level forecasting is difficult.

## Overall Discussion

Overall, Ridge Regression was identified as the most suitable trained ML model because it balanced prediction accuracy, stability, and interpretability. The model captured the general price level of AAPL, but the persistence baseline remained very strong because stock prices are highly continuous over time.

These findings show that next-day stock price prediction is challenging due to market noise and external events. The model is valuable for academic learning and demonstrating the machine learning workflow, but it should not be treated as a reliable trading system or financial investment tool.
