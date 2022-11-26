import paho.mqtt as mqtt
import os
import subprocess

brocker="127.0.0.1"
port=1883
theme="task_2"
mqtt_dir="C:\Program Files\mosquitto"
os.chdir(mqtt_dir)
os.system("mosquitto_sub -h "+brocker+" -t "+theme+" -C 3")
print(subprocess.getoutput())