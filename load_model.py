import joblib

model = joblib.load("employee_model.pkl")

prediction = model.predict([[45, 80000]])

print("Prediction:", prediction)
