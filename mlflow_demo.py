import mlflow

mlflow.set_experiment("customer-churn-demo")

with mlflow.start_run():

    mlflow.log_param("learning_rate", 0.001)
    mlflow.log_param("epochs", 20)

    mlflow.log_metric("accuracy", 0.91)
    mlflow.log_metric("loss", 0.09)

    print("Run logged successfully")
