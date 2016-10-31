#visualisation using external values
#PLEASE NOTE: movement speed variables may need to be adjusted - increased(i think) for mac
#I HAVE INCLUDED VIDEO IN GITHUB REPOS (pcVis.mp4) PROVING PC ANIMATION WORKS
#for mac run visualisation 1 by pressing '1' key on keyboard
'''On a good PC press '2' key on keyboard for second visualisation.
Is slow on macs but perfect on decent PC
circles radius is controlled by grades/data - speed also controlled by data;
bigger/higher grades have higher chance of being faster'''

from graphics import *
import time
import random
new_color = color_rgb(220,50,255)
allTheBalls = []


with open("data.txt", "r") as data:
    #Get all words numbers (as strings) from data, store in data_num variable as a list
    data_num = data.read().split("\n")
    data.close()

user_choice = raw_input("Press '1' for mac visualisation, or '2' for PC visualisation (need a decent PC fo this)")


window = GraphWin("Visualisation", 800, 500)
if (user_choice == '2'):
    print("You chose the PC visualisation")
    def new_rand_pos():
        randomX = random.randint(0, 800)
        randomY = random.randint(0, 500)
        return Point(randomX,randomY)

    def build_item(pos, radius):
        global ball, allTheBalls
        ball = Circle(pos, radius)
        ball.setFill(color_rgb(220,50,255))
        ball.xspeed = ((random.random()*2.0) - 1.0) * radius / 40
        ball.yspeed = ((random.random()*2.0) - 1.0) * radius / 40
        ball.setOutline("purple")
        ball.draw(window)
        allTheBalls.append(ball)
        #pass in colors control with animate_item

    def animate_item(b, color):
        currentPosition = b.getCenter()
        if(currentPosition.getX() <= 0.0 ):
            b.xspeed = -b.xspeed
            color = color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            b.setFill(color)
            
        if(currentPosition.getX() >= 800.0 ):
            b.xspeed = -b.xspeed
            color = color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            b.setFill(color)
            
        if(currentPosition.getY() <= 0.0 ):
            b.yspeed = -b.yspeed
            color = color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            b.setFill(color)
            
        if(currentPosition.getY() >= 500.0 ):
            b.yspeed = -b.yspeed
            color = color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            b.setFill(color)
        b.move(b.xspeed,b.yspeed)

    for i in range(len(data_num)):
        new_radius = int(data_num[i])/2
        # print(data_num[i])
        build_item(new_rand_pos(), new_radius)

    #print(allTheBalls)
        
    while True:
        for i in allTheBalls:
            animate_item(i, new_color)

else:
    print("You chose the Mac visualisation")
    plane_x = 1
    plane_y = 0
    background1 = Image(Point(400,250), "background1.gif")
    background1.draw(window)
       
    while True:
        for planes in range(len(data_num)):
            grade = int(data_num[planes])

            if grade <= 50:
                which_plane = 3
            elif grade > 50 and grade <= 60:
                which_plane = 2
            elif grade > 60 and grade <= 70:
                which_plane = 1
            else:
                which_plane = 0
                
            text = Text(Point(400,20),"Grade: " + data_num[planes])
            text.setFace('helvetica')
            text.setSize(20)
            text.setFill(color_rgb(255,255,255))
            text.setStyle('bold')
            text.draw(window)
            
            plane = Image(Point(random.randrange(60,740), 550 -grade * 5 ), "plane"+str(which_plane)+".gif")
            plane.draw(window)
            time.sleep(0.5)# sleep between each plane
            background = Image(Point(400,250), "background.gif")
            background.draw(window)

        time.sleep(0.1)
