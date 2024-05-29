import os
from pymongo import MongoClient

client = MongoClient('mongodb://mongo:27017')
db = client["pedidos_casal_lanches"]
