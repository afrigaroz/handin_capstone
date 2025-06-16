# build_dummy_model.py

"""
This script generates a dummy machine learning model and saves it to model/model.pkl.
It allows the xG prediction pipeline to function before real model training is complete.
"""

from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Ensure the model folder exists
os.makedirs("model", exist_ok=True)

# Dummy data: 2 samples with 5 features
X_dummy = [
    [0, 0, 0, 0, 0],  # Fake example → not a goal
    [1, 1, 1, 1, 1]   # Fake example → goal
]
y_dummy = [0, 1]

# Train a very basic classifier
model = RandomForestClassifier()
model.fit(X_dummy, y_dummy)

# Save model to disk
joblib.dump(model, "model/model.pkl")

print(" Dummy model saved to model/model.pkl")
