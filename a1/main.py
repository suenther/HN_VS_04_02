from fastapi import FastAPI
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_products(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8082/products")
        products = response.json()
    return templates.TemplateResponse("products.html", {
        "request": request,
        "products": products
    })
