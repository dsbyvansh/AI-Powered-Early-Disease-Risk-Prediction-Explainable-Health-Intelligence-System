# AI Powered Diabetes Risk Prediction

I am predicting diabetes risk using BRFSS 2011-2015 survey data.
This is a screening tool for anyone who wants an early risk check and lifestyle guidance.

## Example data (used in this project)
- Survey-based inputs (no personal identifiers)
- Basic: Age group, Sex, Height, Weight, BMI
- Lifestyle: Smoking status, Alcohol use, Exercise, Mental health days
- Health status: General health, Physical health days
- Medical history: Heart attack, stroke, arthritis, kidney disease, cancer, depression, asthma
- Healthcare access: Insurance, personal doctor, cost barriers, last checkup

## Meaning Of Risk Prediction
- Risk prediction here means estimating a probability and mapping it to a risk category (low/medium/high).
- The model uses survey patterns, not clinical tests like HbA1c.
- This is a binary classification problem (diabetes risk yes/no).

## Objective
- Build a reliable screening model that flags higher-risk users for further testing.
- Provide simple risk categories and top contributing factors for transparency.

## Data Source
- CDC BRFSS 2011-2015 survey data from Kaggle.
- Large-scale, self-reported public health survey (not clinical lab data).

## Output
- A probability score and a risk category (low/medium/high).
- Short explanation of top risk-increasing and risk-reducing factors.

## Scope
- Adults covered by BRFSS survey responses.
- Risk screening only, not diagnosis or treatment advice.

## Success Criteria
- Prioritize recall to reduce missed high-risk cases.
- Maintain reasonable ROC-AUC and stable performance across splits.

## Confusion Matrix Clarity
- A confusion matrix is a performance measurement tool for machine learning classification algorithms.
- Key Components:
    - True Positive (TP): Correctly predicted positive instance.
    - True Negative (TN): Correctly predicted negative instance.
    - False Positive (FP): Incorrectly predicted positive (Type 1 Error).
    - False Negative (FN): Incorrectly predicted negative (Type 2 Error).

A False Negative here means the model missed a person who is actually at risk.
In healthcare screening, FN is usually more costly than FP, so recall is prioritized.
