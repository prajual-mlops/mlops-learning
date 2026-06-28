import mlflow
import mlflow.sklearn
from sklearn.tree import DecisionTreeClassifier

x = [
    [25, 30000],
    [40, 70000],
    [35, 50000],
    [28, 35000]
]

y = [0, 1, 1, 0]

mlflow.set_experiment("employee-retention-model")

with mlflow.start_run():

    model = DecisionTreeClassifier(max_depth=3)
    model.fit(x,y)

    mlflow.log_param("max_depth", 3)

    mlflow.sklearn.log_model(
        sk_model=model,
        name="employee-retention-model"
    )

    print("Model registered successfully")


