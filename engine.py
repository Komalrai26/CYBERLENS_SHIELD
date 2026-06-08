import joblib

# Load your model (ensure model.pkl is in the same folder!)
model = joblib.load('model.pkl')

def get_prediction(url):
    # IMPORTANT: You must convert the URL to the exact feature format 
    # your model was trained on here.
    # For now, let's return a dummy result to test the connection:
    return "Safe"