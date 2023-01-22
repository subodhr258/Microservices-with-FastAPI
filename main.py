from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:3000'],
allow_methods = ['*'],
allow_headers = ['*'])

redis = get_redis_connection(
    host = "redis-17159.c301.ap-south-1-1.ec2.cloud.redislabs.com",
    port = 17159,
    password = "fzTahPHzkpWgTtKmNMCOB1BIvdgOrRLL",
    decode_responses = True
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

@app.get("/products")
def all():
    return Product.all_pks()