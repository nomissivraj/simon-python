from mosquitto import *
from serial import *
from random import *

def messageReceived(broker, obj, msg):
    global client
    receive_payload = msg.payload.decode()
    if (receive_payload == "ON"):
        payload = "1"
    else:
        payload = "0"
    board.write(payload.encode())


board = Serial("/dev/cu.usbmodem14432",115200,timeout=2)

randomID = random()
client = Mosquitto("LightSubscriber" + str(randomID))
client.connect("10.212.61.136")
client.subscribe("/lights")
client.on_message = messageReceived

while (True): client.loop()