import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
import joblib

BASE_DIR = Path(__file__).parent

# Load training data
X_train = pd.read_csv(BASE_DIR / "X_train.csv")
y_train = pd.read_csv(BASE_DIR / "y_train.csv").squeeze()

# Create the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, BASE_DIR / "medication_model.pkl")

print("Model training completed successfully!")
print("Trained model saved as medication_model.pkl")