# создать отдельные функции

import sys
import os
import time
import numpy as np
import math
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


class Bot():
    message = """'cmd':'{}''val':'{}'"""
    def __init__(self, v=2.0, omega=2.0,
                 mqtt_ip="127.0.0.1", mqtt_port=1883, mqtt_theme="practice_1", filepath="path.txt"):
        self.currentAngle = 0
        self.v = v
        self.omega = omega
        self.mqtt_ip = mqtt_ip
        self.mqtt_port = mqtt_port
        self.mqtt_theme = mqtt_theme
        self.file_path = filepath
        if not os.path.exists(self.file_path):
            raise FileExistsError("File not found")
        else:
            self.path = np.loadtxt(self.file_path, dtype=float)
        self.move()

    def distanceCount(self, newCoords):
        return math.sqrt((newCoords[0] - self.coords[0]) ** 2 + (newCoords[1] - self.coords[1]) ** 2)

    def angleCount(self, newCoords):
        def alphaCheck(alpha):
            if alpha>=360:
                alpha-=360
            elif alpha<=-360:
                alpha+=360
            return math.fabs(alpha)
        return alphaCheck(math.degrees(
            math.atan2(newCoords[1] - self.coords[1], newCoords[0] - self.coords[0])) - self.currentAngle)
    def move(self):
        def forward(distance):
            cmd="forward"
            val=distance/self.v
            commandPublish(cmd, val)
        def back(distance):
            cmd="back"
            val=distance/self.v
            commandPublish(cmd, val)
        def right(angle):
            cmd = "right"
            val = abs(angle) / self.omega
            commandPublish(cmd, val)
        def left(angle):
            cmd="left"
            val=angle/self.omega
            commandPublish(cmd,val)
        def commandPublish(cmd,val):
            client.publish(self.message.format(cmd, val))
            time.sleep(val)
        mqtt.Client.connected_flag = False
        client = mqtt.Client("practice_1")
        client.on_connect = on_connect
        print("Connecting to brocker ", self.mqtt_ip)
        client.connect(self.mqtt_ip, self.mqtt_port)
        print("start loop")
        for i in range(1,len(self.path)):
            self.coords = self.path[i-1]
            angle=self.angleCount(self.path[i])
            distance=self.distanceCount(self.path[i])
            if angle==0:
                forward(distance)
            elif 0<angle<180:
                left(angle)
                forward(distance)
            elif angle==180:
                back(distance)
            elif 180<angle<359:
                right(angle)
                forward(distance)
        message = """'cmd':'stop'"""
        client.publish(self.mqtt_theme, message)
        client.disconnect()

if __name__ == '__main__':
    command = sys.argv
    bot_1 = Bot(float(command[4]), float(command[5]),command[1],int(command[2]),command[3],command[6])
# python botcontrol.py 127.0.0.1 1883 abotcmd1 1.0 30.0 path.txt
