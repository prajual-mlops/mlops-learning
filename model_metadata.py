import json

model = {
    "model_name": "customer_churn_model",
    "version": "1.0",
    "accuracy": 0.92,
    "status": "production"
}

with open("model.json","w") as file:
    json.dump(model, file, indent=4)

print("Model metadata saved")
