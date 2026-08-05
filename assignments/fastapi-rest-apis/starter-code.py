from typing import Optional

from fastapi import FastAPI, HTTPException, Query, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST API Assignment")


class Product(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)
    in_stock: bool = True


products: dict[int, Product] = {}


@app.get("/")
def read_root():
    # TODO Task 1: Return a JSON welcome message
    return {"message": "Welcome to the FastAPI assignment API"}


@app.get("/health")
def health_check():
    # TODO Task 1: Keep this endpoint simple for API checks
    return {"status": "ok"}


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    # TODO Task 2: Prevent duplicate IDs and store the product
    if product.id in products:
        raise HTTPException(status_code=400, detail="Product ID already exists")
    products[product.id] = product
    return product


@app.get("/products", response_model=list[Product])
def list_products(in_stock: Optional[bool] = Query(default=None)):
    # TODO Task 4: Add support for filtering by stock using ?in_stock=true|false
    if in_stock is None:
        return list(products.values())
    return [product for product in products.values() if product.in_stock == in_stock]


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    # TODO Task 2: Return 404 when product_id is not found
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    # TODO Task 3: Keep the route ID and body ID consistent
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    products[product_id] = updated_product
    return updated_product


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    # TODO Task 3: Return 404 when trying to delete a missing product
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    del products[product_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
