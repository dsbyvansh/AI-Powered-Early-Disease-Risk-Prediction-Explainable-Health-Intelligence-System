# AI Powered Diabetes Risk Prediction System 

## Overview
***An end to end AI powered Diabetes ~~Diagnosis~~ risk prediction system , It uses a form based approach to take the users data and predicts their risk of diabetes by using the BRFSS 2011-2015 data consisting of 2M+ CDC survey responses***

## Key Features
1) System built on the data of 2M+ real people
2) This system uses machine learning to predict your diabetes risk
3) User friendly form based approach (just enter your details and youre good to go) 
## Tech Stack
- **Numpy** and **Pandas** for data analysis
- **Matplotlib** and **Seaborn** for data visualization
- **Scikit-Learn** for preprocessing and machine Learning
- **Tensor Flow(keras)** for deep learning
- **Shap** for explainability
- **Streamlit** for a clean web app

## Project Structure (folder tree)
- .streamlit
- app
- data
    - processed
    - raw
- models
- notebooks
- reports
    - univariate analysis
    - bivariate analysis
    - statistical analysis
    - model
    - explainability
- problem_statement.md
- README.md

## Dataset
- Source: CDC BRFSS 2011-2015 (Kaggle)
- Raw: 2,380,047 rows, 158 cols
- Final cleaned: 2,018,571 rows, 34 features + 1 target
- Train: 1,614,856 rows | Test: 403,715 rows 
- Class balance: 84% no diabetes, 16% diabetes

## Methodology (8-week roadmap summary)
- Week 1: Problem definition + data collection + Feature engineering + preprocessing pipeline
- Week 2: EDA + statistical analysis + Train and compare ML models + Deep learning model + Explainable AI + error analysis
- Week 3: Web app (Streamlit)
- Week 4: Final polish + documentation <- ongoing

## Model Performance
| Model | ROC-AUC | Recall (t=0.5) | Notes |
|---|---|---|---|
| Logistic Regression | 0.801 | 0.74 | Good baseline |
| Decision Tree | 0.802 | 0.77 | Simple, interpretable |
| Random Forest (tuned) | 0.807 | 0.75 | Ensemble, robust |
| KNN | 0.690 | 0.19 | Poor — subsample + imbalance |
| XGBoost (final) ⭐ | 0.808 | 0.76 | Best performer |
| SVM | N/A | N/A | Skipped — too slow on 2M rows |
| Neural Network | 0.807 | 0.83 | Close but XGBoost wins on tabular |

## How to Run
### 1) Clone the repo
```
git clone <your-repo-url>
cd Project
```

### 2) Create and activate a virtual environment
```
python -m venv .venv
.venv\Scripts\activate
```

### 3) Install dependencies
```
pip install numpy pandas scikit-learn tensorflow shap joblib streamlit matplotlib seaborn xgboost
```

### 4) Download the dataset
1) Download CDC BRFSS 2011-2015 from Kaggle.
2) Place the five yearly CSVs inside `data/raw/`:
    - 2011.csv
    - 2012.csv
    - 2013.csv
    - 2014.csv
    - 2015.csv

### 5) Run the notebooks in order
Open the notebooks under `notebooks/` and run cells in this order:
1) `initial_inspection.ipynb`
2) `preprocessing.ipynb`
3) `feature_selection.ipynb`
4) `eda.ipynb`
5) `statistical_analysis.ipynb`
6) `model_training.ipynb`
7) `deep_learning.ipynb`
8) `explainability.ipynb`

### 6) Launch the Streamlit app
```
streamlit run app/app.py
```

## Limitations
- Trained on 2011-2015 BRFSS data; results may drift on newer populations.
- Self-reported survey data can contain bias and reverse causality.
- Screening-only: predictions are not a medical diagnosis.
- Class imbalance limits precision; threshold tuned for higher recall.
- Does not include lab measurements (e.g., HbA1c, fasting glucose).

## Future Improvements
- Retrain on newer BRFSS data.
- Add a requirements file for easy setup.
- Improve the UI and explanation visuals.
- Add basic automated tests.

## Author
Author: [dsbyvansh](https://github.com/dsbyvansh) | [X](https://x.com/pywithvansh)
