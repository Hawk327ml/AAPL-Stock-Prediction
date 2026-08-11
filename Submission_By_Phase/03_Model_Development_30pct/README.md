# AAPL Model Development

Open `AAPL_Model_Development.ipynb` and run all cells from this folder.

The notebook reads the bundled `data/AAPL_Prepared_for_Modeling.csv` and writes:

- evaluation tables to `results/`;
- charts to `figures/`;
- the selected fitted pipeline and metadata to `models/`.

The experiment uses 2015-2022 for training and time-series cross-validation, 2023 for model selection, and 2024 for the final test.

The bundled `data/` file is the main data source for the presentation.
