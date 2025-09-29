
from ex_db import MONGO_URI
from pymongo import MongoClient

client = MongoClient(MONGO_URI)

db = client["cloud_inventory"]

collection_1 = db["product"]
collection_2 = db["customers"]
collection_3 = db["users"]
collection_4 = db["sales"]


