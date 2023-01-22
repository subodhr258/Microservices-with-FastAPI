from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel

app = FastAPI()

redis = get_redis_connection(
    host = "redis-17159.c301.ap-south-1-1.ec2.cloud.redislabs.com:17159",
    port = 11844,
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
    return []