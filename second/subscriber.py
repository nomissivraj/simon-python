#Flash LED's when receiving 'ON' from server

from mosquitto import *
from serial import *
from random import *

def messageReceived(broker, obj, msg):
    global client
    receive_payload = msg.payload.decode()
    '''If message recieved evaluates to ON set payload for micro bit to '1' as code flashed
    onto the micro bit is listening for either 1 or 0 to opperate on since behavior
    was weird otherwise'''
    if (receive_payload == "ON"):
        payload = "1"
    else:
        payload = "0"
    board.write(payload.encode())

#connect to microbit serial port
board = Serial("/dev/cu.usbmodem14432",115200,timeout=2)
#Connect to server
randomID = random()
client = Mosquitto("LightSubscriber" + str(randomID))
client.connect("10.212.61.136")
client.subscribe("/lights")
#run function to handle message when recieving something
client.on_message = messageReceived

while (True): client.loop()
