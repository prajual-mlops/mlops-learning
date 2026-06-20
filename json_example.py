import json

model = {
    "model_name": "customer-churn-model",
    "version": "1.0",
    "accuracy": 0.92
}

json_data = json.dumps(model, indent=4)

print(json_data)
