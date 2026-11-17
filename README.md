# DiaCheck — Diabetes Risk Prediction

A machine-learning web application that estimates diabetes risk from user-provided health indicators. The project demonstrates a complete introductory ML workflow, from data exploration and preprocessing to model evaluation and a Flask-based prediction interface.

> **Important:** This is an educational prediction project, not a medical diagnostic tool. Predictions should not be used to make healthcare decisions.

## Project overview

DiaCheck accepts health-related inputs and passes them through a trained scikit-learn model to generate a binary prediction. The documented input fields include pregnancies, glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function and age.

## Workflow

1. **Data preparation** — gather and inspect the dataset.
2. **Exploratory analysis** — examine distributions and relationships between health indicators.
3. **Preprocessing** — clean and transform data for modelling.
4. **Model training** — build a classification model with scikit-learn.
5. **Evaluation** — assess model performance using classification metrics.
6. **Web interface** — collect inputs through a Flask application and display the prediction.

## Technology

- Python
- pandas
- scikit-learn
- Flask

## Run locally

The application entry point is `app.py`.

```bash
git clone https://github.com/arpitaengineer08-source/DiaCheck.git
cd DiaCheck
pip install -r requirements.txt
python app.py
```

Open the local URL printed by Flask in your terminal (commonly `http://127.0.0.1:5000`).

## Input features

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Glucose measurement |
| Blood pressure | Blood pressure measurement |
| Skin thickness | Skin-fold thickness |
| Insulin | Insulin measurement |
| BMI | Body mass index |
| Diabetes pedigree function | Dataset-provided family-history indicator |
| Age | Age in years |

Use the exact feature order and preprocessing expected by the model files in this repository.

## Scope and limitations

- Model predictions depend on the training dataset and its representativeness.
- Performance on a public dataset does not establish clinical validity.
- This project is intended for learning and demonstration only.

## Author

**Arpita Sharma** — B.Tech, Computer Science and Engineering (Data Science & AI)
