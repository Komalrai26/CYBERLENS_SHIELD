import os
print("I am looking for files in this folder:")
print(os.getcwd())
print("Files I can see here are:")
print(os.listdir())
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Load the data
df = pd.read_csv('/Users/komalrai/Desktop/CyberLens_Shield/PhisingURLDataset.csv')

# 2. Separate into "Clues" (X) and "Answer" (y)
X = df.drop('phishing', axis=1) # Everything except the 'phishing' column
y = df['phishing']               # Just the 'phishing' column

# 3. Split the data (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Create and train the "Brain"
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Check how smart the "Brain" is
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
import joblib

# This 'dumps' (saves) your trained model object to a permanent file
joblib.dump(model, 'model.pkl')
print("\nModel saved as model.pkl! The dashboard can now use it.")

print(f"CyberLens Shield has been trained!")
print(f"Accuracy Score: {accuracy * 100:.2f}%")
print(df.columns.tolist())