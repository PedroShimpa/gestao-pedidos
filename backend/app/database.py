import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGODB_URL"))
db = client["pedidos_casal_lanches"]
