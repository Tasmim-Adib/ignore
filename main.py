from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schema import Products

app = FastAPI()

#import services
from database import(
    fetch_one_product,
    add_product
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/product/{category}", response_model = Products)
async def get_product_by_category(category):
    response = await fetch_one_product(category)
    if response:
        return response
    raise HTTPException(404, f"There is no product on {category}")

@app.post("/product", response_model = Products)
async def save_product(product : Products):
    response = await add_product(product.model_dump())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")