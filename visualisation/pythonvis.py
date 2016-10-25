#visualisation using external values
from graphics import *
import time
import random

allTheBalls = []

with open("data.txt", "r") as data:
    #Get all words numbers (as strings) from data, store in data_num variable as a list
    data_num = data.read().split("\n")
    data.close()

window = GraphWin("Visualisation", 800, 500)

def new_rand_pos():
    randomX = random.randint(0, 800)
    randomY = random.randint(0, 500)
    return Point(randomX,randomY)

def build_item(pos, radius):
    global ball, allTheBalls
    ball = Circle(pos, radius)
    ball.setFill(color_rgb(255,255,0))
    ball.xspeed = ((random.random()*2.0) - 1.0) * 20.0
    ball.yspeed = ((random.random()*2.0) - 1.0) * 20.0
    ball.draw(window)
    allTheBalls.append(ball)

def animate_item(b):
    currentPosition = b.getCenter()
    if(currentPosition.getX() <= 0.0 ): b.xspeed = -b.xspeed
    if(currentPosition.getX() >= 800.0 ): b.xspeed = -b.xspeed
    if(currentPosition.getY() <= 0.0 ): b.yspeed = -b.yspeed
    if(currentPosition.getY() >= 500.0 ): b.yspeed = -b.yspeed
    b.move(b.xspeed,b.yspeed)

for i in range(len(data_num)):
    new_radius = int(data_num[i])/2
    # print(data_num[i])
    build_item(new_rand_pos(), new_radius)

#print(allTheBalls)
    
while True:
    for i in allTheBalls:
        animate_item(i)

#window = GraphWin("Visualisation", 800, 500)
#vertices = [50, 75, 100]
#shape1 = Polygon(Point(50,50), Point(10,200), Point(100,100))
#shape1.setFill(color_rgb(0,255,0))
#shape1.draw(window)
#time.sleep(100)