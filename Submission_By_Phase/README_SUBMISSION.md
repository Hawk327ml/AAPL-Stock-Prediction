# Group 13 CSM3601 Project Submission

Project title: Stock Price Prediction Using Machine Learning  
Dataset/topic: AAPL stock price prediction using supervised regression

## Folder order

1. `00_Project_Sheet/`
   - Original course project sheet.

2. `01_Proposal_10pct/`
   - Group 13 project proposal in PDF and DOCX format.
   - Covers project title, problem statement, objectives, proposed dataset, proposed algorithms, and expected outcome.

3. `02_Data_Preparation_EDA_20pct/`
   - `AAPL_Data_Preparation.ipynb`: data collection, cleaning, missing value handling, duplicate checks, and cleaned CSV export.
   - `AAPL_Data_Preparation_EDA_Final.ipynb`: EDA, visualization, outlier inspection, correlation analysis, leakage-aware feature engineering, chronological split, and modeling CSV export.
   - `AAPL_Cleaned.csv` and `AAPL_Prepared_for_Modeling.csv`: final data files used by later phases.

4. `03_Model_Development_30pct/`
   - Full standalone model-development files and `Model_Development.zip`.
   - Includes train/validation/test split, cross-validation, pipelines, at least three ML models, hyperparameter tuning, overfitting comparison, saved model, figures, and result tables.

5. `04_Evaluation_Discussion_20pct/`
   - Evaluation notebook/package plus the main model discussion.
   - Includes MAE, MSE, RMSE, R2 Score, directional accuracy, best-model discussion, strengths/weaknesses, feature importance, and ethical considerations.

6. `05_Presentation_Demonstration_20pct/`
   - Contains the presentation/demo guide and figure assets for the poster or notebook demo.
   - Since the instructor confirmed that slides are not required, use `README_PRESENTATION_DEMO.md` as the main speaking path.

7. `99_Archive_Not_For_Presentation/`
   - Original backups, old drafts, and compressed source files.
   - Kept for traceability, but not part of the normal presentation flow.

## Recommended inspection path

Open this README first, then use `05_Presentation_Demonstration_20pct/README_PRESENTATION_DEMO.md` for tomorrow's speaking flow.

For code review, the two most important notebooks are:

- `02_Data_Preparation_EDA_20pct/AAPL_Data_Preparation_EDA_Final.ipynb`
- `03_Model_Development_30pct/AAPL_Model_Development.ipynb`

## Key result summary

- Locked ML model: Ridge Regression.
- Selection rule: lowest 2023 validation RMSE among trained ML models before looking at the 2024 test set.
- 2024 test performance for Ridge Regression: MAE 2.1196, RMSE 2.8764, R2 0.9873, directional accuracy 49.00%.
- Persistence baseline slightly outperforms Ridge on 2024 RMSE, which is acknowledged in the discussion because next-day stock price levels are highly autocorrelated.
- For presentation, focus on the course-aligned workflow: data cleaning, EDA, feature engineering, model comparison, evaluation, and responsible interpretation. Do not over-emphasize advanced methods from the early proposal.
