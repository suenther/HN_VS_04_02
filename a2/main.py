from fastapi import FastAPI
app = FastAPI()

FAKE_PRODUCTS = [
{"name": "Produkt A", "price": 9.99},
{"name": "Produkt B", "price": 19.99}
]
@app.get("/products")
def get_products():
    return FAKE_PRODUCTS