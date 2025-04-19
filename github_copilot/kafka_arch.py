from kafka import KafkaProducer
import time
import json

# Kafka Producer Configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Kafka Topic
topic = 'logs'

# Dummy Kafka Messages
messages = [
    {"timestamp": "2023-01-01T12:00:00", "level": "INFO", "message": "Application started"},
    {"timestamp": "2023-01-01T12:01:00", "level": "ERROR", "message": "An error occurred"},
    {"timestamp": "2023-01-01T12:02:00", "level": "DEBUG", "message": "Debugging application"}
]

# Sending Messages to Kafka
for message in messages:
    producer.send(topic, message)
    print(f"Sent: {message}")
    time.sleep(1)

producer.close()

