from sklearn.tree import DecisionTreeClassifier
import joblib

x = [
    [25, 30000],
    [40, 70000],
    [35, 50000],
    [28, 35000]
]

y = [0, 1, 1, 0]

model = DecisionTreeClassifier()

model.fit(x, y)

joblib.dump(model, "employee_model.pkl")

print("Model saved successfully")
