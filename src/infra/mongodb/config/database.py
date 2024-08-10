from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("mongodb_url"))
db = client.db1
collection_name = db['exercises']