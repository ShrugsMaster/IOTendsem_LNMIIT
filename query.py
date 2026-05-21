import json
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

device_id = "sensor_01"

redis_key = f"device:{device_id}:readings"

readings = redis_client.lrange(redis_key, 0, 9)

temperatures = []

for item in readings:
    data = json.loads(item)

    print(data)

    temperatures.append(data["value"])

if temperatures:
    average = sum(temperatures) / len(temperatures)

    print(f"Average Temperature: {average:.2f}")
else:
    print("No readings found")