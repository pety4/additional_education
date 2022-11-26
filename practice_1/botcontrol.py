import sys
import os
import time
import numpy as np
import turtle
import math
import paho.mqtt as mqtt



def distance(x,y,x1,y1):
    return math.sqrt((x1-x)**2+(y1-y)**2)
def angle(x,y,x1,y1):
    return math.atan2(y1-y,x1-x)
if __name__ == '__main__':
    """command=sys.argv
    mqtt_ip=command[2]
    mqtt_port=command[3]
    mqtt_theme=command[4]
    v=float(command[5])
    omega=float(command[6])
    file=command[7]"""
    #command = sys.argv
    mqtt_ip = "127.0.0.1"
    mqtt_port = "1883"
    mqtt_theme = "bot_1"
    v = 3.0
    omega = 30.0
    file_path = "path.txt"
    if not os.path.exists(file_path):
        print("File not found")
    else:
        path=np.loadtxt(file_path, dtype=float)
    turtle.setposition(path[0][0],path[0][1])
    print(turtle.position())
    turtle.left(angle(path[0][0],path[0][1],path[1][0],path[1][1]))
    print(angle(path[0][0],path[0][1],path[1][0],path[1][1]))
    turtle.forward(distance(path[0][0],path[0][1],path[1][0],path[1][1]))
    print(distance(path[0][0],path[0][1],path[1][0],path[1][1]))
    print(turtle.position())
    turtle.exitonclick()