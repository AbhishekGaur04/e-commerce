from fastapi import FastAPI
from routes import product_routes, order_routes

app = FastAPI()

app.include_router(product_routes.router)
app.include_router(order_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce API"}
