# Project Context for Claude Code

## Project
AI-Powered Early Diabetes Risk Prediction System

## Goal
End-to-end ML/DL project for internship preparation. Predicts diabetes risk using the 
CDC BRFSS dataset (2011-2015) from Kaggle.

## Mentor Style
- Act as a senior data science mentor
- Guide step by step — do NOT give full solutions unless explicitly asked
- Ask interview-style questions to check understanding
- Suggest best practices and industry norms
- Help debug approach, not just code
- Maintain full technical memory of all decisions, tradeoffs, and reasoning
- Think like an interviewer preparing cross-questions at all times

## Current Status
Week 7 — COMPLETED ✅
Week 8 — Starting next (Final Polish + Documentation + Master Handbook)

## Completed So Far
- [x] Project folder structure created
- [x] Raw dataset downloaded (CDC BRFSS 2011-2015, 5 CSVs)
- [x] problem_statement.md written
- [x] README.md created
- [x] CLAUDE.md context file created
- [x] All 5 CSVs merged (2.38M rows, 158 cols → common 157 cols)
- [x] Survey_year column added
- [x] Target variable DIABETE3 mapped to binary (1/2/4→1, 3→0)
- [x] Sentinel values handled throughout (7/9/77/99/888 etc)
- [x] Feature selection complete (157 → 34 cols, 3-layer approach)
- [x] PNEUVAC3 removed — reverse causality confirmed by SHAP
- [x] Missing values handled (imputation + row dropping)
- [x] Full sentinel audit completed
- [x] Binary encoding complete (BRFSS 1/2 → ML 1/0)
- [x] EDA complete (univariate, bivariate, correlation heatmap)
- [x] Reverse causality documented for 5+ features
- [x] Hypothesis testing (t-test BMI, chi-square Exercise/Depression)
- [x] Confidence intervals + Cohen's d (d=0.66, medium effect for BMI)
- [x] Probability distributions identified (log-normal BMI, Poisson PHYSHLTH, Bernoulli target)
- [x] CLT validated t-test results despite non-normal BMI
- [x] Bayes theorem — P(Diabetes|HighBMI) = 26.17% vs prior 14.85%
- [x] Train/test split (80/20 stratified)
- [x] Preprocessing pipeline built (StandardScaler, OrdinalEncoder, passthrough)
- [x] Preprocessor saved to models/preprocessor.pkl
- [x] ML models trained: LR, DT, RF, KNN, XGBoost (SVM skipped)
- [x] GridSearchCV tuning for RF and XGBoost
- [x] Threshold tuning — final threshold=0.40
- [x] SMOTE skipped — class_weight='balanced' sufficient at 2M scale
- [x] Neural network built (TF/Keras, 2 hidden layers, dropout, batch norm)
- [x] ML vs DL comparison complete — XGBoost wins
- [x] SHAP explainability — summary plot, waterfall plot, feature importance
- [x] PNEUVAC3 removed post-SHAP — reverse causality confirmed
- [x] XGBoost retrained on 34 features — ROC-AUC=0.808
- [x] All models saved to models/
- [x] Streamlit app built and working end-to-end
- [x] Risk categories defined (Low/Medium/High)
- [x] SHAP explanations integrated into app
- [x] Recommendations section added

## Dataset
- Source: CDC BRFSS 2011-2015 (Kaggle)
- Raw: 2,380,047 rows, 158 cols
- Final cleaned: 2,018,571 rows, 34 features + 1 target
- Train: 1,614,856 rows | Test: 403,715 rows
- Class balance: 84% no diabetes, 16% diabetes

## Feature Sets (Final — 34 features)
- Binary (22): _RFBING5, _AIDTST3, HLTHPLN1, QLACTLM2, CHCOCNCR,
  _RFHLTH, HAVARTH3, HIVTST6, MEDCOST, CHCSCNCR, EXERANY2, DRNKANY5,
  _HCVU651, ADDEPEV2, PERSDOC2, CVDSTRK3, _TOTINDA, CHCKIDNY,
  CVDCRHD4, CVDINFR4, SEX, _DRDXAR1
- Continuous (4): PHYSHLTH, _BMI5, ALCDAY5, MENTHLTH
- Ordinal (8): _SMOKER3, GENHLTH, _AGEG5YR, INCOME2, EDUCA,
  _ASTHMS1, CHECKUP1, _CHLDCNT

## Model Performance Summary
| Model | ROC-AUC | Recall (t=0.5) | Notes |
|---|---|---|---|
| Logistic Regression | 0.801 | 0.74 | Good baseline |
| Decision Tree | 0.802 | 0.77 | Simple, interpretable |
| Random Forest (tuned) | 0.807 | 0.75 | Ensemble, robust |
| KNN | 0.690 | 0.19 | Poor — subsample + imbalance |
| XGBoost (final) ⭐ | 0.808 | 0.76 | Best performer |
| SVM | N/A | N/A | Skipped — too slow on 2M rows |
| Neural Network | 0.807 | 0.83 | Close but XGBoost wins on tabular |

## Key Design Decisions & Rationale
- **Binary classification** — diabetic yes/no (pre-diabetics mapped to 1)
- **Pre-diabetics → 1** — screening tool goal, intervention before onset
- **PNEUVAC3 removed** — reverse causality (diabetics prescribed vaccine)
- **Threshold = 0.40** — healthcare context, FN more costly than FP
- **SMOTE skipped** — 364K minority samples sufficient, class_weight used
- **SVM skipped** — computationally infeasible on 1.6M training rows
- **XGBoost over NN** — tabular data favors gradient boosting
- **Precision ceiling ~0.28-0.32** — fundamental 84/16 imbalance limitation
- **Evaluation priority** — ROC-AUC, Recall, F2 over accuracy
- **StandardScaler** — chosen over MinMaxScaler due to outliers in BMI/ALCDAY5
- **OrdinalEncoder fitted on original BRFSS values** — app must send
  pre-encoded BRFSS values (1-based), not post-encoded (0-based)

## Critical Debugging Lessons (For Handbook)
- OrdinalEncoder fitted on INPUT values not OUTPUT — always verify
  with `named_transformers_['ordinal'].categories_[i]`
- Always save preprocessor separately from model
- `astype(float)` required before preprocessor.transform() in app
- Column order in input_df must match binary+continuous+ordinal order
- SHAP feature_names must use all_cols order not input_dict key order
- Streamlit caching with @st.cache_resource prevents model reload
- Conditional widgets inside st.form() cause persistence bugs

## XGBoost Final Parameters
- n_estimators: 200
- max_depth: 4
- learning_rate: 0.05
- scale_pos_weight: 5.719
- threshold: 0.40

## App Architecture
User Input (Streamlit form)
- Mapping (BRFSS codes)
- Derived features (_RFHLTH, _TOTINDA, etc.)
- DataFrame assembly (34 features, correct column order)
- astype(float)
- preprocessor.transform() [StandardScaler + OrdinalEncoder]
- model.predict_proba() [XGBoost]
- threshold=0.40
- Risk category (Low/Medium/High)
- SHAP explanation (top contributors)
- Recommendations

## Temporal Validity Limitations
- Model trained on 2011-2015 data — temporal covariate shift by 2025
- Post-COVID behavioral changes not captured
- GLP-1 medications (Ozempic/Wegovy) not in training population
- Diabetes demographic shift toward younger population not captured
- Requires periodic retraining on recent BRFSS data for production use

## 8-Week Roadmap
- Week 1: Problem definition + data collection ✅
- Week 2: EDA + statistical analysis ✅
- Week 3: Feature engineering + preprocessing pipeline ✅
- Week 4: Train and compare ML models ✅
- Week 5: Deep learning model ✅
- Week 6: Explainable AI + error analysis ✅
- Week 7: Web app (Streamlit) ✅
- Week 8: Final polish + documentation + Master Handbook ← NEXT

## Saved Artifacts
- data/processed/cleaned_data.csv
- data/processed/x_train.csv, x_test.csv, y_train.csv, y_test.csv
- models/preprocessor.pkl
- models/xgboost_final.pkl
- models/random_forest_tuned.pkl
- models/neural_network.keras
- reports/univariate/, reports/bivariate/, reports/statistical/
- reports/shap_summary.png, shap_importance.png
- app/app.py