from kafka import KafkaConsumer
KAFKA_BROKER = 'localhost:9092'
TOPIC = 'app-logs'
OUTPUT_FILE = 'errors_only.log'
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    group_id='log-group',
    value_deserializer=lambda x: x.decode('utf-8')
)
print("Consumer started...")
for message in consumer:
    log_line = message.value
    if "ERROR" in log_line.upper():
        with open(OUTPUT_FILE, 'a') as file:
            file.write(log_line + '\n')
        print(f"Logged ERROR: {log_line}")