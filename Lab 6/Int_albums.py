import pymongo

MONGO_URI = "mongodb+srv://macababbaddennis0:156324987@cluster0.gwwuu8f.mongodb.net/"
client = pymongo.MongoClient(MONGO_URI)
db = client["Lab6_PostLabs"]
album_collection = db["albums"]

albums_data = [
    {"Title": "Love Story", "ArtistId": "Artist1"},
    {"Title": "Flash Light", "ArtistId": "Artist2"},
    {"Title": "You & I", "ArtistId": "Artist3"},
    {"Title": "Thriller", "ArtistId": "Artist4"},
    {"Title": "Gyutto", "ArtistId": "Artist5"},
]

for album in albums_data:
    result = album_collection.insert_one(album)
    print("Inserted document ID:", result.inserted_id)

client.close()