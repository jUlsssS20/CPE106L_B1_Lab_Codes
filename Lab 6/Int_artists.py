import pymongo

MONGODB_URI = "mongodb+srv://macababbaddennis0:156324987@cluster0.gwwuu8f.mongodb.net/"
DB_NAME = "Lab6_PostLabs"
COLLECTION_NAME = "artists"

artists_data = [
    {"Name": "Taylor Swift"},
    {"Name": "Jessie J."},
    {"Name": "One Direction"},
    {"Name": "Michael Jordan"},
    {"Name": "Gyutto"},
]

with pymongo.MongoClient(MONGODB_URI) as client:
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    result = collection.insert_many(artists_data)

    print("Inserted document IDs:", result.inserted_ids)