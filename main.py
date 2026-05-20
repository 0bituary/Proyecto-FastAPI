from fastapi import FastAPI

app = FastAPI()

products=[
    {"id":1,"name":"Laptop", "price": 1200},
    {"id":2,"name":"Mouse", "price": 25},
    {"id":3,"name":"Keyboard", "price": 80},
    {"id":4,"name":"Monitor", "price": 300},
    {"id":5,"name":"Headphones", "price": 150}
]

#@app.get("/products")
#def get_products():
#    return products

@app.get("/products/{id}")
def get_products_id(id:int):
    for product in products:
        if product ["id"]==id:
            return product

@app.get("/products")
def get_products_query(limit:int=5):
    return {"limit":limit}

