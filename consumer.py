from kafka import KafkaConsumer

# Create a Kafka consumer instance
consumer = KafkaConsumer('my-topic', bootstrap_servers='localhost:9092')

# Continuously poll for new messages
for message in consumer:
    print(message.value.decode())

# Close the consumer
consumer.close()
