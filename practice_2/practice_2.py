from paho.mqtt import client as mqtt_client
import json
import math
import os


class App():
    brocker = "127.0.0.1"
    port = 1883
    clien_id = "bot_1"
    topic = "practice_1"
    command = ''

    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to mqtt brocker")
            else:
                print("Failed to connect")

        client = mqtt_client.Client(self.clien_id)
        client.on_connect = on_connect
        client.connect(self.brocker, self.port)
        return client

    def subscribe(self, client: mqtt_client):
        def on_message(client, userdata, msg):
            message = msg.payload.decode()
            print(message)
            print(f"Received '{message}' from '{msg.topic}' topic")
            self.command = json.loads(message)
            print(self.command['cmd'])
            print(self.command['val'])
            self.move()

        client.subscribe(self.topic)
        client.on_message = on_message


class RobotModel(App):
    logFile = 'logs.csv'
    x = 0
    y = 0
    alpha = 0
    v = 5.0
    omega = 30.0
    time = 0

    def __init__(self):
        if not os.path.exists(self.logFile):
            raise FileExistsError("'Could not open/read file: ", self.logFile)
        self.client = self.connect_mqtt()
        self.subscribe(self.client)
        self.client.loop_forever()

    def move(self):
        def alphaCheck():
            if self.alpha >= 360:
                self.alpha -= 360
            elif self.alpha <= -360:
                self.alpha += 360
            self.alpha = math.fabs(self.alpha)

        def distanceCount(time):
            return time * self.v

        def alphaCount(time):
            return time * self.omega

        def deltCount(time):
            return math.cos(math.radians(self.alpha)) * distanceCount(time), \
                   math.sin(math.radians(self.alpha)) * distanceCount(time)

        def forward(time):
            dx, dy = deltCount(time)
            if 0 <= self.alpha <= 90:
                self.x += dx
                self.y += dy
            elif 90 < self.alpha <= 180:
                self.x -= dx
                self.y += dy
            elif 180 < self.alpha <= 270:
                self.x -= dx
                self.y -= dy
            elif 270 < self.alpha <= 359:
                self.x += dx
                self.y -= dy

        def back(time):
            dx, dy = deltCount(time)
            if 0 <= self.alpha <= 90:
                self.x -= dx
                self.y -= dy
            elif 90 < self.alpha <= 180:
                self.x += dx
                self.y -= dy
            elif 180 < self.alpha <= 270:
                self.x += dx
                self.y += dy
            elif 270 < self.alpha <= 359:
                self.x -= dx
                self.y += dy

        def right(time):
            self.alpha -= alphaCount(time)
            alphaCheck()

        def left(time):
            self.alpha += alphaCount(time)
            alphaCheck()

        if (self.command['cmd'] == 'forward'):
            forward(float(self.command['val']))
        if (self.command['cmd'] == 'back'):
            back(float(self.command['val']))
        if (self.command['cmd'] == 'right'):
            right(float(self.command['val']))
        if (self.command['cmd'] == 'left'):
            left(float(self.command['val']))
        self.time += float(self.command['val'])
        with open(self.logFile, "a") as f:
            f.write(f'\n{round(self.time, 3)};{round(self.x, 3)};{round(self.y, 3)};{round(self.alpha, 3)}')
        print(f'time={self.time};\n'
              f'x={self.x};\n'
              f'y={self.y};\n'
              f'alpha={self.alpha}')


if __name__ == '__main__':
    bot_1 = RobotModel()

