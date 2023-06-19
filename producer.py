from kafka import KafkaProducer

# Create a Kafka producer instance
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send a message to a Kafka topic
producer.send('my-topic', b'Hello, Kafka!')

# Flush the producer to make sure the message is sent
producer.flush()

# Close the producer
producer.close()
