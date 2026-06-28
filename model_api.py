from fastapi import FastAPI
import joblib


app = FastAPI()


model = joblib.load("employee_model.pkl")


@app.get("/")
def home():
    return {"message": "Employee Prediction API"}


@app.get("/predict")
def predict():

    prediction = model.predict([[45, 80000]])

    return{
        "prediction": int(prediction[0])
    }
