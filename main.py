from fastapi import FastAPI
from pydantic import BaseModel

# ✅ FIRST define app
app = FastAPI()

# Input model
class House(BaseModel):
    area: float
    bedrooms: int

# Home API
@app.get("/")
def home():
    return {"message": "API is running"}

# Prediction API
@app.post("/predict-price")
def predict_price(data: House):
    price = (data.area * 0.5) + (data.bedrooms * 10)
    return {
        "predicted_price": price
    }