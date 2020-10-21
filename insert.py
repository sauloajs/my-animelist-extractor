from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['my-anime-list']
collection = db.animes

with open('animes.json') as json_file:
    animes = json.load(json_file)
    ids = collection.insert_many(animes).inserted_ids
    print('This script inserted ' + str(len(ids)) + ' objects')
    