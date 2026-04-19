# DataCo Smart Supply Chain Analytics

## Project Objective

This project builds a complete data pipeline for supply chain analytics using the **DataCo Smart Supply Chain** dataset. The pipeline covers:

- Exploratory Data Analysis (EDA)
- Data cleaning and transformation with PySpark
- Relational storage in PostgreSQL
- Interactive dashboards with Power BI
- Demand forecasting with XGBoost
- Risk simulation with Monte Carlo
- Final reporting and presentation (Sprint 7)

---

## Dataset

The dataset is available on Kaggle:  
[DataCo Smart Supply Chain Dataset](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)

Place the CSV file in `data/raw/` – it is ignored by Git (large file).

---

## Environment Setup

### Tools

| Tool       | Version       | Notes                           |
|------------|---------------|---------------------------------|
| Python     | 3.11.9        | Added to PATH                   |
| Java (JDK) | 17.0.14 LTS   | Required for PySpark            |
| PySpark    | 3.5.2         | Installed via pip               |
| PostgreSQL | 16.13         | Port 5432                       |
| VS Code    | 1.109.0       | Main IDE                        |

### Installation verification

#### Python
```bash
python --version
# ✔️ Python 3.11.9
```

#### Java (JDK 17)
```bash
java --version
# ✔️ Java correctly installed, JAVA_HOME set
```

#### PySpark
```bash
python -m pip install pyspark==3.5.2
python -c "import pyspark; print(pyspark.__version__)"
# ✔️ Version 3.5.2 detected
```

#### PostgreSQL
- Local installation, port 5432, accessible via pgAdmin
- ✔️ Connection to `localhost` validated

#### VS Code
Extensions used: Python (Microsoft), PostgreSQL

---

## Project Structure

```
.
├── data/
│   ├── raw/               # raw CSV (ignored)
│   └── staging/           # Parquet files (cleaned, split, features)
├── notebooks/             # EDA notebook
├── src/                   # PySpark / Python scripts
├── sql/                   # schema, validation, indexes
├── docs/                  # ERD, UML, sprint reports
├── powerbi/               # .pbix dashboard file
├── models/                # saved XGBoost models
├── reports/               # final outputs (PDF, etc.)
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── .env.example
└── requirements.txt
```

---

## Pipeline Overview (Sprints 1–7)

| Sprint | Focus |
|--------|-------|
| 1 | Environment setup, EDA, ERD design, cleaning decisions |
| 2 | Data cleaning (PySpark) and splitting into normalised tables (Parquet) |
| 3 | PostgreSQL schema creation, data loading, validation, indexing |
| 4 | Power BI dashboards (Sales, Logistics, Customers, Profitability) |
| 5 | XGBoost demand forecasting (feature engineering, training, evaluation) |
| 6 | Monte Carlo simulation for stockout risk and safety stock |
| 7 | UML diagrams, final report, and presentation |

All scripts, notebooks, and the Power BI dashboard are versioned in this repository.

---

## Getting Started

1. Clone the repository.
2. Install Python dependencies: `pip install -r requirements.txt`.
3. Download the dataset and place it in `data/raw/`.
4. Run the cleaning script: `python src/cleaning.py`.
5. Run the split script: `python src/split_tables.py`.
6. Create the PostgreSQL database and tables using `sql/schema.sql`.
7. Load data into PostgreSQL: `python src/load_postgres.py`.
8. Open `powerbi/supply_chain.pbix` in Power BI Desktop.
9. For ML, run `src/feature_engineering.py` then `src/train_and_simulate.py`.

---

## License & Acknowledgements

This project was developed for academic purposes. The dataset is provided by DataCo on Kaggle.
