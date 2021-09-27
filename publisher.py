#!/usr/bin/env python

import paho.mqtt.client as mqtt
import cayenne.client
import json
import os
import sys
import time
from dotenv import load_dotenv
from info import Info

load_dotenv()

user = os.getenv('MQTT_USER')
password = os.getenv('MQTT_PASSWORD')
server = os.getenv('MQTT_SERVER')
port = int(os.getenv('MQTT_PORT'))
client_id = sys.argv[1] 
# client_id = os.getenv('MQTT_CLIENT_ID')

client = cayenne.client.CayenneMQTTClient()
client.begin(user, password, client_id, port = port)

while True:
    obj = Info.gen_new()

    client.loop()
    client.virtualWrite(1, obj.temp, "temp", "c")
    client.virtualWrite(2, obj.humidity, "rel_hum", "Percent")
    client.virtualWrite(3, obj.digital_sensor(), "digital_sensor", "Digital")

    time.sleep(5)

client.loop_forever()