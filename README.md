🧩 Home Assistant + MQTT Integration (Nakshatra Automation Assignment)
Student Details

Name: Monish M

Register Number: 42110819

MQTT Topic Used: home/monishm42110819-2025/sensor

Project Overview

This project demonstrates integration between a Python script, a local Mosquitto MQTT broker, and Home Assistant running on macOS via Docker. The Python script publishes sensor values to an MQTT topic, and Home Assistant subscribes to that topic and visualizes the data on a dashboard.

Sensors Published

The script publishes the following values every 5 seconds:

Temperature: Random variation around 25°C

Humidity: Random variation around 60%

Light Sensor: 0 or 1 (represents OFF/ON)


