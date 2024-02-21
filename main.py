from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route using a Python decorator
@app.get("/")  # Decorator defines a GET request handler for the root path
def read_root():
    return {"message": "Hello, world!"}

# @app.get("/items/{item_id}")  # Route parameter is specified using curly braces
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
