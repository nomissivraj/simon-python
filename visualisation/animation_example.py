from graphics import *

window = GraphWin("Visualisation", 300, 300)
ball = Circle(Point(100,300), 20)
ball.setFill(color_rgb(255,255,0))
xspeed = 1.5
yspeed = 1.5
ball.draw(window)

while True:
    currentPosition = ball.getCenter()
    if(currentPosition.getX() <= 0 ): xspeed = -xspeed
    if(currentPosition.getX() >= 300 ): xspeed = -xspeed
    if(currentPosition.getY() <= 0 ): yspeed = -yspeed
    if(currentPosition.getY() >= 300 ): yspeed = -yspeed
    ball.move(xspeed,yspeed)