
# Model Card: Student Learning Prediction

## Model Purpose
This model demonstrates student pass/fail prediction
using a synthetic educational dataset.

## Intended Use
Educational learning and machine learning demonstration only.

## Target Variable
passed:
- 0 = Fail
- 1 = Pass

## Input Features
- hours_studied
- attendance
- practice_tests
- sleep_hours
- study_method

## Excluded Feature
final_score was excluded to prevent data leakage.

## Models Evaluated
- Dummy Classifier
- Logistic Regression
- Random Forest Classifier

## Selected Model
See evaluation_summary.md for the selected model and metrics.

## Limitations
The dataset is synthetic and contains only 280 records.
Its results may not represent real student performance.

## Ethical Considerations
This model must not be used for real student grading,
admission, punishment, or other high-impact decisions.
