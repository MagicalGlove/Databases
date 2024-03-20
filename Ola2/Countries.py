from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://user:password420@ola2cluster.bijj3hs.mongodb.net/")

db = cluster["ola2db"]
collection = db["Countries"]

collection.insert_one({"_id":0, "name":"Test"})