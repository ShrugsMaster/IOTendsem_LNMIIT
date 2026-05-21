import json
import redis
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/temperature"

redis_client = redis.Redis(host="localhost", port=6379, db=0)

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())

    device_id = payload["device_id"]

    redis_key = f"device:{device_id}:readings"

    redis_client.lpush(redis_key, json.dumps(payload))

    redis_client.ltrim(redis_key, 0, 999)

    print(payload)

client = mqtt.Client()

client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.subscribe(TOPIC)

client.loop_forever()