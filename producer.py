from kafka import KafkaProducer
import time

KAFKA_BROKER = 'localhost:9092'
TOPIC = 'app-logs'
LOG_FILE = 'app.log'
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: v.encode('utf-8')
)
try:
    with open(LOG_FILE, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                producer.send(TOPIC, value=line)
                print(f"Sent: {line}")
            time.sleep(1)  

except FileNotFoundError:
    print(f"Error: Log file '{LOG_FILE}' not found.")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    producer.flush()
    producer.close()