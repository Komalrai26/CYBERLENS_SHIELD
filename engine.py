import joblib
import pandas as pd

# Load your model once
model = joblib.load('model.pkl')

def analyze_url(url):
    # Perform your feature engineering here
    # ... logic ...
    prediction = model.predict(data)
    return prediction