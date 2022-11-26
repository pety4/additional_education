import paho.mqtt.client as mqtt
import os
import time

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

mqtt.Client.connected_flag=False
brocker="127.0.0.1"
port=1883
client=mqtt.Client("programm1")
client.on_connect=on_connect
print("Connecting to brocker ", brocker)
client.connect(brocker,port)
client.loop_start()
while not client.connected_flag:
    print("in wait loop")
    time.sleep(1)
print("in Main loop")
if not os.path.exists("mqtt_message.txt"):
    print("file not found")
else:
    file=open("mqtt_message.txt","r")
    message=file.read().splitlines()
    file.close()
for string in message:
    client.publish("task_2",string)
time.sleep(1)
client.loop_stop()
client.disconnect()
