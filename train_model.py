import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load data
df = pd.read_csv("kaggle_diabetes.csv")

# Prepare X, y
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Train model (or use your existing trained model)
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
with open("diabetes_model.pkl", "wb") as f:
    pickle.dump(model, f)