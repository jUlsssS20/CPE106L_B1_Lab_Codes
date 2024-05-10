import pymongo

MONGODB_URI = "mongodb+srv://macababbaddennis0:156324987@cluster0.gwwuu8f.mongodb.net/"
DB_NAME = "Lab6_PostLabs"
COLLECTION_NAME = "tracks"

with pymongo.MongoClient(MONGODB_URI) as client:
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    for document in collection.find():
        print("{")
        for key, value in document.items():
            print(f"  {key}: {value}")
        print("}")
        print()