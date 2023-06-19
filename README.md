# MongoDB Change Detection with Kafka

This project develops two applications, a producer and a consumer. The producer application queries a specified MongoDB collection every 10 seconds for new documents and publishes a JSON message for each new document to a Kafka topic. The consumer application consumes messages from the Kafka topic and prints them to the console.

## Technologies Used

-   Python
-   Docker
-   Apache Kafka
-   ZooKeeper
-   Kafdrop
-   MongoDB: Used the Change Stream functionality to watch for changes.

## Build Steps

1. Clone this repository: `git clone https://github.com/HussainMhm/MongoDB-Kafka-CDC`
2. Navigate to the project directory: `cd MongoDB-Kafka-CDC`
3. Build the Docker images: `docker-compose build`
4. Start the Docker services: `docker-compose up -d`

## Running the Applications

After starting the Docker services, the producer and consumer applications will begin running automatically. The producer will check the MongoDB collection for new documents every 10 seconds and publish any new documents to the Kafka topic. The consumer will consume messages from the Kafka topic and print them to the console.

## License

This project is licensed under the [MIT License](LICENSE).
