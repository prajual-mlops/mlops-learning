from fastapi import FastAPI

app = FastAPI()

model_info = {
    "model_name": "customer_churn_model",
    "version": "1.0",
    "accuracy": 0.92,
    "status": "production"
}

@app.get("/")
def home():
    return{"message":"Hello MLOps"}

@app.get("/health")
def health():
    return{
        "status": "healthy",
        "service": "mlops-learning"
    }

@app.get("/model-info")
def get_model_info():
    return model_info

@app.get("/metrics")
def metrics():
    return{
        "requests_today": 124,
        "avg_response_time_ms": 32,
        "error_rate": 0.01
    }

@app.get("/server")
def server():
    return{
        "server": "mlflow-server",
        "cpu": 78,
        "memory": 90
    }
