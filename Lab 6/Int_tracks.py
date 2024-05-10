import pymongo

tracks_data = [
    {
        "Name": "Love Story",
        "AlbumId": "Object",
        "MediaTypeId": 1,
        "GenreId": 1,
        "Composer": "Taylor Swift",
        "Milliseconds": 240000,
        "Bytes": 11200420,
        "UnitPrice": 5.29,
    },
    {
        "Name": "Flashlight",
        "AlbumId": "Object",
        "MediaTypeId": 1,
        "GenreId": 1,
        "Composer": "Jessie J.",
        "Milliseconds": 230000,
        "Bytes": 19871354,
        "UnitPrice": 4.20,
    },
    {
        "Name": "You & I",
        "AlbumId": "Object",
        "MediaTypeId": 1,
        "GenreId": 1,
        "Composer": "One Direction",
        "Milliseconds": 243000,
        "Bytes": 33147921,
        "UnitPrice": 6.50,
    },
    {
        "Name": "Thriller",
        "AlbumId": "Object",
        "MediaTypeId": 1,
        "GenreId": 1,
        "Composer": "Michael Jackson",
        "Milliseconds": 805200,
        "Bytes": 11353481,
        "UnitPrice": 8.99,
    },
    {
        "Name": "Gyutto",
        "AlbumId": "Object",
        "MediaTypeId": 1,
        "GenreId": 1,
        "Composer": "Mosawo",
        "Milliseconds": 258000,
        "Bytes": 11359484,
        "UnitPrice": 3.50,
    },
]

with pymongo.MongoClient("mongodb+srv://macababbaddennis0:156324987@cluster0.gwwuu8f.mongodb.net/") as client:
    db = client["Lab6_PostLabs"]
    collection = db["tracks"]

    result = collection.insert_many(tracks_data)

    for idx, inserted_id in enumerate(result.inserted_ids, start=1):
        print(f"Inserted document ID ({idx}): {inserted_id}")