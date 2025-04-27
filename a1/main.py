from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()

templates = Jinja2Templates(directory="app/views/templates")

@app.get("/")
async def read_products(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:9002/products")
        products = response.json()
        print(products)
        return templates.TemplateResponse("products.html", {"request": request, "products": products})
