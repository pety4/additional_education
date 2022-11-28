import sys
import os
import time
import numpy as np
import math
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

class Bot():
    def __init__(self, coords, v=0, omega=0):
        self.coords = coords
        self.currentAngle = 0.0
        self.v = v
        self.omega = omega

    def distance(self, newCoords):
        return math.sqrt((newCoords[0] - self.coords[0]) ** 2 + (newCoords[1] - self.coords[1]) ** 2)

    def angle(self, newCoords):
        return (math.degrees(
            math.atan2(newCoords[1] - self.coords[1], newCoords[0] - self.coords[0])) - self.currentAngle)


if __name__ == '__main__':
    command = sys.argv
    mqtt_ip = command[1]
    mqtt_port = int(command[2])
    mqtt_theme = command[3]
    v = float(command[4])
    omega = float(command[5])
    file_path = command[6]

    if not os.path.exists(file_path):
        print("File not found")
    else:
        path = np.loadtxt(file_path, dtype=float)
    bot_1 = Bot([path[0][0], path[0][1]], v, omega)
    mqtt.Client.connected_flag = False
    client = mqtt.Client("practice_1")
    client.on_connect = on_connect
    print("Connecting to brocker ", mqtt_ip)
    client.connect(mqtt_ip, mqtt_port)
    client.loop_start()
    message = """'cmd':'{}''val':'{}'"""
    for i in range(1, len(path)):
        bot_1.coords = path[i - 1]
        df = bot_1.angle(path[i])
        distance = bot_1.distance(path[i])
        if -90 <= df <= 90:
            if df > 0:
                cmd = "left"
                v = df
                client.publish(message.format(cmd, v))
                time.sleep(v*bot_1.omega)
                bot_1.currentAngle += df
            if df < 0:
                cmd = "right"
                v = abs(df)
                client.publish(message.format(cmd, v))
                time.sleep(v*bot_1.omega)
                bot_1.currentAngle += df
            cmd = "forward"
            v = distance
            client.publish(message.format(cmd, v))
            time.sleep(v*bot_1.v)
        else:

            if df > 90 or df < -90:
                df_reverse = bot_1.angle(-path[i])
                if df_reverse > 0:
                    cmd = "right"
                    v = df_reverse
                    client.publish(message.format(cmd, v))
                    time.sleep(v * bot_1.omega)
                    bot_1.currentAngle += df
                if df_reverse < 0:
                    cmd = "left"
                    v = df_reverse
                    client.publish(message.format(cmd, v))
                    #time.sleep(v * bot_1.omega)
                    bot_1.currentAngle += df_reverse
                cmd = "back"
                v = distance
                client.publish(mqtt_theme,message.format(cmd, v))
                time.sleep(v * bot_1.v)

    message = """'cmd':'stop'"""
    client.publish(mqtt_theme, message)
    client.loop_stop()
    client.disconnect()+