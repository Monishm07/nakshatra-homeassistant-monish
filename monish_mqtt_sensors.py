
import json
import time
import paho.mqtt.client as mqtt

# ---- Required by assignment ----
student_name = "Monish M"
unique_id = "42110819"
topic = "home/monishm42110819-2025/sensor"   # DO NOT CHANGE THIS

# ---- MQTT Broker details ----
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

try:
    while True:
        # Static values as per assignment
        temperature = 25       # °C
        humidity = 60          # %
        light = 1              # 1 = ON, 0 = OFF (extra sensor)

        payload = {
            "student_name": student_name,
            "unique_id": unique_id,
            "temperature": temperature,
            "humidity": humidity,
            "light": light
        }

        json_payload = json.dumps(payload)
        result = client.publish(topic, json_payload)

        status = result[0]
        if status == 0:
            print(f"Published to {topic}: {json_payload}")
        else:
            print(f"Failed to send message to topic {topic}")

        time.sleep(5)   # Publish every 5 seconds

except KeyboardInterrupt:
    print("Stopping publisher...")

finally:
    client.loop_stop()
    client.disconnect()

