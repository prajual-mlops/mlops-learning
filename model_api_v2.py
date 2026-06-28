from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("employee_model.pkl")


@app.get("/")
def home():
    return {
        "message": "Employee Prediction API"
    }


@app.get("/predict")
def predict(age:int, salary:int):

    prediction = model.predict([[age, salary]])

    return {
        "age": age,
        "salary": salary,
        "prediction": int(prediction[0])
    }
