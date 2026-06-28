import mlflow
import joblib

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

x_train = [
    [25, 30000],
    [40, 70000],
    [35, 50000],
    [28, 35000]
]

y_train = [0, 1, 1, 0]

x_test = [
    [50, 90000],
    [27, 32000]
]

y_test = [1, 0]

mlflow.set_experiment("employee-retention-model")

with mlflow.start_run():

    model = DecisionTreeClassifier(max_depth=3)

    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)

    joblib.dump(model, "employee_model.pkl")

    mlflow.log_param("max_depth", 3)
    mlflow.log_metric("accuracy", accuracy)

    mlflow.log_artifact("employee_model.pkl")

    print("Model artifact logged successfully")
