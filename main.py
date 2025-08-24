from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import csv
from backend import add_expense
import pandas as pd

API_KEY = "saurabh_123"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=404, details= "Invalid API Key")
    return True

class Item(BaseModel):
    date: str = Field(...,description="Write a date in DD-MM-YYYY format: ")
    name: str = Field(...,description= "write the name of the item purchased")
    quantity: int = Field(..., description = "Write the quantity of the item purchased")
    price: float = Field(..., description= "Write the price of each item")

app = FastAPI()

@app.post("/add_expense",response_model=Item)
def add(new_item: Item):
    try:
        add_expense(new_item.date,new_item.name,new_item.quantity,new_item.price)
        return new_item
    except Exception as e:
        raise HTTPException(status_code=500,detail= str(e))
    
@app.get("/show_data",response_model=Item)
def show_data():
    df = pd.read_csv("D:/Python Projects/Personal Expense Tracker/expense_tracker.csv")
    data = df.to_dict()

    return JSONResponse(content=data)