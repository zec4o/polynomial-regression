from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Create a class with the input data model
class request_body(BaseModel):
  months_of_service: int
  seniority: int

# Load the model
poly_model = joblib.load('./salary_model.pkl')

@app.post('/predict/')
def predict_salary(data : request_body):

  input_features = {
  'months_of_service': data.months_of_service,
  'seniority': data.seniority,
  }

  pred_df = pd.DataFrame(input_features, index=[1])

  y_pred = poly_model.predict(pred_df)[0].astype(float).round(2)

  return {'salary_in_brl': y_pred.tolist()}
