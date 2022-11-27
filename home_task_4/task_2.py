import paho.mqtt as mqtt
import os
import subprocess

brocker="127.0.0.1"
port=1883
theme="task_2"
mqtt_dir="C:\Program Files\mosquitto"
os.chdir(mqtt_dir)
while(True):
    mqtt_get=subprocess.getoutput("mosquitto_sub -h " + brocker + " -t " + theme + " -C 3")
    v=[float(i) for i in mqtt_get.splitlines()]
    movingAverage=0.6*v[2]+0.3*v[1]+0.1*v[0]
    print("Moving average: ", movingAverage)