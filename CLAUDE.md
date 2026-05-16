# Project Context for Claude Code

## Project
AI-Powered Early Disease Risk Prediction & Explainable Health Intelligence System

## Goal
End-to-end ML/DL project for internship preparation. Predicts diabetes risk using the 
CDC BRFSS dataset (~250K rows, 21 features) from Kaggle (Alex Teboul).

## Mentor Style
- Act as a senior data science mentor
- Guide step by step — do NOT give full solutions unless explicitly asked
- Ask interview-style questions to check understanding
- Suggest best practices and industry norms
- Help debug approach, not just code

## Current Status
Week 3, Day 8 — COMPLETED ✅
Week 4, Day 9 — Starting next (ML Model Training begins)

## Completed So Far
- [x] Project folder structure created
- [x] Raw dataset downloaded and placed in data/raw/
- [x] problem_statement.md written
- [x] README.md created
- [x] CLAUDE.md context file created
- [x] First GitHub commit pushed
- [x] All 5 CSVs loaded and inspected
- [x] Common columns identified (157)
- [x] merged_df created (2.38M rows, 158 cols)
- [x] Survey_year column added
- [x] Target variable (DIABETE3) mapped and cleaned
- [x] Missing value analysis
- [x] Feature selection
- [x] Univariate analysis (BMI distribution)
- [x] Bivariate analysis (BMI, Exercise, Physical Health vs Diabetes)
- [x] Outlier detection and removal (BMI > 60)
- [x] Sentinel value handling during EDA (EXERANY2, PHYSHLTH)
- [x] Zero-inflation identified in PHYSHLTH
- [x] Plots saved to reports/
- [x] T-test: BMI vs Diabetes (p < 0.001)
- [x] Chi-square: Exercise vs Diabetes (p < 0.001)
- [x] Chi-square: Depression vs Diabetes (p < 0.001)
- [x] 95% Confidence Intervals for BMI groups
- [x] Non-overlapping CIs confirm BMI discriminative power
- [x] Probability distributions identified
- [x] Bayes theorem applied
- [x] Binary encoding complete (1/2 → 1/0)
- [x] Final sentinel audit complete
- [x] Train/test split (80/20 stratified)
- [x] Preprocessing pipeline built (StandardScaler, OrdinalEncoder)
- [x] x_train, x_test, y_train, y_test saved to data/processed/

## Dataset
- Final shape: 2,018,571 rows, 36 cols
- Train: 1,614,856 rows
- Test: 403,715 rows
- Class balance: 84% no diabetes, 16% diabetes

## Feature Sets
- Binary (23): _RFBING5, _AIDTST3, HLTHPLN1, QLACTLM2, CHCOCNCR,
  _RFHLTH, HAVARTH3, HIVTST6, MEDCOST, CHCSCNCR, EXERANY2, DRNKANY5,
  _HCVU651, ADDEPEV2, PERSDOC2, CVDSTRK3, _TOTINDA, CHCKIDNY,
  CVDCRHD4, CVDINFR4, SEX, _DRDXAR1, PNEUVAC3
- Continuous (3): PHYSHLTH, _BMI5, ALCDAY5
- Ordinal (9): _SMOKER3, GENHLTH, MENTHLTH, _AGEG5YR, INCOME2,
  EDUCA, _ASTHMS1, CHECKUP1, _CHLDCNT

## 8-Week Roadmap
- Week 1: Problem definition + data collection ✅
- Week 2: EDA + statistical analysis ✅
- Week 3: Feature engineering + preprocessing pipeline ✅
- Week 4: Train and compare ML models ← NEXT
- Week 5: Deep learning model
- Week 6: Explainable AI + error analysis
- Week 7: Web app (Streamlit or Flask)
- Week 8: Final polish + documentation

## Tech Stack
Python, NumPy, Pandas, Matplotlib, Seaborn, scikit-learn, 
TensorFlow/Keras or PyTorch, SHAP, LIME, Streamlit or Flask

## Key Design Decisions
- Binary classification problem (diabetes: yes/no)
- Dataset is large enough to justify deep learning
- Healthcare context means False Negatives are more costly than False Positives
- Class imbalance must be handled explicitly
- Evaluation priority: ROC-AUC, Recall, F1 over plain accuracy
