from pymongo import MongoClient

client = MongoClient("mongodb+srv://thyroid:project@ahmad.5gjdl.mongodb.net/patient_database?retryWrites=true&w=majority\")
db = client.get_database('mydatabase')