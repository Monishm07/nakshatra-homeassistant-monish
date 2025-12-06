import json
import time
import random
import paho.mqtt.client as mqtt


student_name = "Monish M"
unique_id = "42110819"
topic = "home/monishm42110819-2025/sensor"


BROKER = "localhost"   # Mosquitto is running on your Mac
PORT = 1883
KEEPALIVE = 60

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker")
    else:
        print(f"❌ Failed to connect, return code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT, KEEPALIVE)
client.loop_start()


temperature = 25.0   # °C
humidity = 60.0      # %

light = 1            # start as ON

try:
    while True:  # small drift: -0.5, 0, or +0.5
        temperature += random.choice([-0.5, 0, 0.5])
        humidity += random.choice([-1, 0, 1])

       
        temperature = max(22.0, min(30.0, temperature))
        humidity = max(50.0, min(70.0, humidity))

     
        if random.random() < 0.3:  # 30% chance to flip state
            light = 0 if light == 1 else 1

        payload = {
            "student_name": student_name,
            "unique_id": unique_id,
            "temperature": round(temperature, 1),
            "humidity": round(humidity, 1),
            "light": light
        }

        json_payload = json.dumps(payload)
        result = client.publish(topic, json_payload)

        if result[0] == 0:
            print(f"Published to {topic}: {json_payload}")
        else:
            print(f"Failed to send message to topic {topic}")

        time.sleep(5)  # publish every 5 seconds

except KeyboardInterrupt:
    print("Stopping publisher...")

finally:
    client.loop_stop()
    client.disconnect()


