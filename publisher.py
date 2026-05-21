import json
import time
import random
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/temperature"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

device_id = "sensor_01"

while True:
    payload = {
        "device_id": device_id,
        "value": round(random.uniform(20.0, 35.0), 2),
        "ts": int(time.time())
    }

    message = json.dumps(payload)

    client.publish(TOPIC, message)

    print(message)

    time.sleep(2)