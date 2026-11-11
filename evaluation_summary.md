
# Student Learning Model - Evaluation Summary

## Dataset
Total Records: 280
Training Records: 224
Testing Records: 56

## Target Distribution
Failed Students: 157
Passed Students: 123

## Model Performance

Dummy Classifier:
Accuracy: 0.5536
F1 Score: 0.0000

Logistic Regression:
Accuracy: 0.7500
F1 Score: 0.7200

Random Forest:
Accuracy: 0.7679
F1 Score: 0.7347

## Selected Model
Random Forest

## Feature Selection
hours_studied, attendance, practice_tests,
sleep_hours, study_method

final_score was excluded to prevent data leakage.

## Responsible Use
This project uses synthetic classroom data.
Predictions are for educational demonstration only
and must not be used to judge or penalize real students.
