from kafka import KafkaAdminClient
from kafka.admin import NewTopic
import os

# Get Kafka server from environment variable
server = os.environ['KAFKA_BROKERCONNECT']

def create_topic():
    # Connect to Kafka
    admin_client = KafkaAdminClient(bootstrap_servers=server)

    # Create a new topic
    topic = NewTopic(name='X', num_partitions=1, replication_factor=3)
    admin_client.create_topics(new_topics=[topic])

create_topic()
