from pymongo import MongoClient
import socket

# Simple program to insert data to DB and 
# test the app functionality

def insert_into_db(key, value):
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27020/")
    db = client["mydatabase"]
    collection = db["mycollection"]

    # Insert data into collection
    data = {"key": key, "value": value}
    collection.insert_one(data)

    # Close MongoDB connection
    client.close()

def main():
    # Get key and value from user and insert into MongoDB
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    insert_into_db(key, value)

if __name__ == "__main__":
    main()
