import os
import subprocess

brocker="127.0.0.1"
port=1883
theme="task_2"
mqtt_dir="C:\Program Files\mosquitto"
os.chdir(mqtt_dir)
v=[0,0,0]
while(True):
    mqtt_get=float(subprocess.getoutput("mosquitto_sub -h " + brocker + " -t " + theme + " -C 1"))
    v.pop(2)
    v.insert(0,mqtt_get)
    movingAverage=0.6*v[0]+0.3*v[1]+0.1*v[2]
    print("Moving average: ", movingAverage)