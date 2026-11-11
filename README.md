
# Student Learning Prediction Project

## Project Overview
This project predicts whether a student passes or fails
using a synthetic student learning dataset.



## 🔗 Project Links

### 🌐 Live Streamlit Application
[Open Student Learning Prediction App](https://student-learning-ml-project-gvy9frru96duw62k97vmzy.streamlit.app/)

### 💻 GitHub Repository
[View Source Code on GitHub](https://github.com/ZeenatFatima811/Student-Learning-ML-Project)


## Dataset
File: student_learning.csv

Total records: 280

## Features Used
- hours_studied
- attendance
- practice_tests
- sleep_hours
- study_method

Target: passed

The final_score column was excluded to prevent data leakage.

## Models
- Dummy Classifier
- Logistic Regression
- Random Forest Classifier

## Evaluation
See evaluation_summary.md for model performance metrics.

## Saved Model
student_model.joblib

## New Student Predictions
new_student_records.csv

## Streamlit Application

Install the requirements:

pip install pandas scikit-learn joblib streamlit

Run the application:

streamlit run app.py

## Notebook
Open Assignment_04_ML_Project.ipynb in Google Colab or Jupyter.

## Responsible Use
This project uses synthetic classroom data.
Predictions are for educational demonstration only.
Do not use this model to judge or penalize real students.
