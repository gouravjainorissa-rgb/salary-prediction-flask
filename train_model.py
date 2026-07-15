import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Dataset
data = {
    "experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "salary": [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000]
}

df = pd.DataFrame(data)

# Features
X = df[["experience"]]

# Target
y = df["salary"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Save Model
joblib.dump(model, "salary_model.pkl")

print("Model Saved Successfully!")
