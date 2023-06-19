import os
from kafka import KafkaProducer
from pymongo import MongoClient
from time import sleep
import socket

# Kafka configuration
kafka_topic = 'topic-x'
kafka_bootstrap_servers = os.environ['KAFKA_BROKERCONNECT']
myip = socket.gethostbyname(socket.gethostname())

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)

last_count = 0 
count = 0

# Poll MongoDB and produce messages to Kafka
while(1):
    # Connect to MongoDB
    client = MongoClient('mongodb://mongo:27017/')
    db = client["mydatabase"]
    collection = db["mycollection"]

    # Find all documents in collection and skip previously processed documents
    cursor = collection.find({}, { "key": 1, "value": 1 }).skip(last_count)
    count = collection.count_documents({}) - last_count
    
    for change in cursor:
        # Convert the document to string format and send it to Kafka
        message = str(change)  
        producer.send(kafka_topic, value=message.encode('utf-8'))
        producer.flush()
        print("Message is sent:", change)
        last_document = change

    # Update the count of processed documents
    last_count += count

    # Close MongoDB connection and sleep for 10 seconds before next poll
    client.close()   
    sleep(10)
    
# Close the Kafka producer
producer.close()
