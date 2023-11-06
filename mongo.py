#mongo.py
from pymongo import MongoClient

# Replace <password> with your actual password
connection_string = "mongodb+srv://procar69690:qQDzlwWvdzsapjU9@cluster0.dskdtyr.mongodb.net/?retryWrites=true&w=majority"

# Connect to the cluster
client = MongoClient(connection_string)

# Access a database and a collection
db = client.test_database
collection = db.test_collection

# Example: Insert a document
collection.insert_one({"name": "John Doe", "email": "john@example.com"})
