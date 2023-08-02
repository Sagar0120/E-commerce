from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str


products = [
    Product(id=1, name="Product 1", price=9.99, description="Description 1"),
    Product(id=2, name="Product 2", price=19.99, description="Description 2"),
    Product(id=3, name="Product 3", price=29.99, description="Description 3"),
]


@app.get("/products")
def get_all_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}


@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    for index, p in enumerate(products):
        if p.id == product_id:
            products[index] = product
            return {"message": "Product updated successfully"}
    return {"error": "Product not found"}


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            del products[index]
            return {"message": "Product deleted successfully"}
    return {"error": "Product not found"}


@app.patch("/products/{product_id}")
def update_product_partial(product_id: int, product: Product):
    for index, p in enumerate(products):
        if p.id == product_id:
            updated_product = p.copy(update=product.dict(exclude_unset=True))
            products[index] = updated_product
            return {"message": "Product updated successfully"}
    return {"error": "Product not found"}


@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product created successfully"}
