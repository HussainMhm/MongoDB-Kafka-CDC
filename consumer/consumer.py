from kafka import KafkaConsumer
import os

# Kafka configurations
kafka_topic = 'topic-x'
kafka_group_id = 'group'+os.environ['CONSUMER_ID']
kafka_bootstrap_servers = os.environ['KAFKA_BROKERCONNECT']

# Creating Kafka consumer
consumer = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_bootstrap_servers, group_id=kafka_group_id)

# Start consuming messages
for message in consumer:
    # Decode the received message and print it
    received_message = message.value.decode('utf-8')
    print('Consumer{'+os.environ['CONSUMER_ID'] +'}-- '+'Received:', received_message)

# Close the Kafka consumer
consumer.close()
