from pymongo import MongoClient


def get_mongodb_client():
    client = MongoClient('mongodb://localhost:27017')
    db = client.quotes
    return db
