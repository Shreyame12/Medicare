import pandas as pd
from pathlib import Path
import joblib
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

BASE_DIR = Path(__file__).parent

# Load the trained model
model = joblib.load(BASE_DIR / "medication_model.pkl")

# Load testing data
X_test = pd.read_csv(BASE_DIR / "X_test.csv")
y_test = pd.read_csv(BASE_DIR / "y_test.csv").squeeze()

# Predict results
y_pred = model.predict(X_test)

# Evaluate the model
print("Model Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))