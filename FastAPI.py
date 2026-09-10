# pyright: reportMissingImports=false
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a request body model
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

# Simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# POST endpoint to add an item
@app.post("/items/")
def create_item(item: Item):
    return {"item": item, "status": "Item created successfully"}

# GET endpoint with path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "detail": "Item details here"}
