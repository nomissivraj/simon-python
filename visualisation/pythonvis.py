#visualisation using external values
from graphics import *
import time

window = GraphWin("Visualisation", 800, 500)
vertices = [50, 75, 100]
shape1 = Polygon(Point(50,50), Point(10,200), Point(100,100))
shape1.setFill(color_rgb(0,255,0))
shape1.draw(window)
time.sleep(100)