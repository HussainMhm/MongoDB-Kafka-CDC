import os
from kafka import KafkaProducer
from pymongo import MongoClient
from pymongo.cursor import CursorType
from time import sleep
import socket

# Kafka configuration
myip = socket.gethostbyname(socket.gethostname())
kafka_bootstrap_servers = os.environ['KAFKA_BROKERCONNECT']
kafka_topic = 'topic-x'

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)

# Connect to MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client["mydatabase"]
collection = db["mycollection"]

# Bonus: the MongoDB change stream feature implemented so 
# no need to read files for changes every 10s

# Initialize change stream
change_stream = collection.watch(full_document='updateLookup')

# Start change stream
try:
    print("Watching for changes...")
    for change in change_stream:
        # We're interested in insert operations only
        if change['operationType'] == 'insert':
            # Get the full inserted document
            document = change['fullDocument']
            # Convert the document to string format and send it to Kafka
            message = str(document)
            producer.send(kafka_topic, value=message.encode('utf-8'))
            producer.flush()
            print("Message sent:", document)
except KeyboardInterrupt:
    print("\nStopped.")

finally:
    # Close the MongoDB and Kafka connections
    client.close()
    producer.close()
