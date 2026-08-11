# Member 4 - Ethics, Future Improvements, and Demo

## Main responsibility

Explain ethical considerations, future improvements, and how to demonstrate the project.

## Files to open

- `README_MEMBER4.md`: recommended presentation notes.
Original compressed source material has been moved to `../../99_Archive_Not_For_Presentation/`. Use this README as the clean speaking material.

## Ethical considerations

- The model should not be presented as financial advice.
- A high R2 Score can create false confidence because it does not guarantee correct trading direction.
- Stock prediction may encourage risky decisions if uncertainty is not clearly explained.
- The model does not include sudden events such as earnings surprises, policy changes, or market shocks.
- Users should understand that this is an academic machine learning project.

## Future improvements

- Add market index features such as S&P 500 or NASDAQ.
- Add news sentiment or earnings-event features.
- Use walk-forward retraining to simulate real deployment.
- Build a Streamlit dashboard for interactive demonstration.

## Demo plan

1. Open `03_Model_Development_30pct/AAPL_Model_Development.ipynb`.
2. Show the data split cell: Train, Validation, Test.
3. Show the model comparison table.
4. Show the prediction/residual graph.
5. Show the feature importance graph.
6. End with the ethical warning: not financial advice.

## Short script

For ethical considerations, we should clearly state that this model is not financial advice. Although the R2 Score is high, the directional accuracy is only around 49%, so it cannot reliably tell whether the stock will go up or down. For future work, we can add news sentiment, market index data, and walk-forward retraining. For the live demo, we will show the notebook workflow, the final comparison table, prediction graphs, and feature importance, then explain the limitations responsibly.
