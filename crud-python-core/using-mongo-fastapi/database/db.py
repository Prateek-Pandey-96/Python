import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
task_db = client["taskDB"]
task_col = task_db["tasks"]