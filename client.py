from sockclient import Sockclient
from tkinter import *
import random
import time
from Tank import Tank

my_tank_name = str(random.randint(1,10000))

data = {

    "canvas_width":1000,
    "canvas_height":800}

root = Tk()
mycanvas = Canvas(root,width=data["canvas_width"],height=data["canvas_height"],bg="black")
#tank = c1.create_rectangle(10,10,20,20,fill='green')
mytank = Tank(mycanvas)

def getkey(event):
    #right 
    if(event.keysym == "Right"):
        mytank.move_right()
    #left
    if(event.keysym == "Left"):
        mytank.move_left()
    #up
    if(event.keysym == "Up"):
        mytank.move_up()
    #down
    if(event.keysym == "Down"):
        mytank.move_down()
    #cc.send(mytank.status_json())
    #root.update()
    
tanks = {}

cc = Sockclient(tanks)
cc.start()

mycanvas.focus_set()
mycanvas.bind("<Key>",getkey)
mycanvas.pack()

index = 0

while 1:
    index += 1
    cc.send(mytank.status_json())
    for t in tanks.values():
        if(t.get("tankobj")):
            if(t['delta_x'] or  t['delta_y']):
                mycanvas.move(t["tankobj"],t['delta_x'], t['delta_y'])
                t['pos_x'] += t['delta_x']
                t['pos_y'] += t['delta_y']
                t['delta_x'] = 0
                t['delta_y'] = 0
        else:
            t["tankobj"] = mycanvas.create_rectangle(t["pos_x"],t["pos_y"],t["pos_x"]+20,t["pos_y"]+20,fill=t["color"])
    root.update()
    time.sleep(0.05)




