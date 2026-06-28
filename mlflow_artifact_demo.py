import mlflow

mlflow.set_experiment("customer-churn-demo")

with mlflow.start_run():

    mlflow.log_param("learning_rate", 0.001)
    mlflow.log_metric("accuracy", 0.91)

    mlflow.log_artifact("model_metadata.json")

    print("Artifact uploaded successfully")
