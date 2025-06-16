import json
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.quotes

with open('authors.json', 'r', encoding='utf-8') as f:
    authors = json.load(f)

for author in authors:
    if not db.authors.find_one({'fullname': author['fullname']}):
        db.authors.insert_one(author)

with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quotes': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })
