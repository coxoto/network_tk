from sockclient import Sockclient
from tkinter import *
import random
import time
from Tank import Tank
import platform

root = Tk()
mycanvas = Canvas(root,width=1000,height=800,bg="black")

mytank = Tank()


def getkey(event):
    #right 
    if(platform.system() == 'Windows'):
        if(event.keysym == "Right"):
            mytank.set_direction('right')
            #mytank.move_right()
            
        #left
        if(event.keysym == "Left"):
            mytank.set_direction('left')
            #mytank.move_left()
        
        #up
        if(event.keysym == "Up"):
            mytank.set_direction('up')
            #mytank.move_up()

        #down
        if(event.keysym == "Down"):
            mytank.set_direction('down')
            #mytank.move_down()

    else:
        #right 
        if(event.keycode == 100):
            mytank.set_direction('right')
            #mytank.move_right()
        #left
        if(event.keycode == 97):
            mytank.set_direction('left')
            #mytank.move_left()
        #up
        if(event.keycode == 119):
            mytank.set_direction('up')
            #mytank.move_up()
        #down
        if(event.keycode == 115):
            mytank.set_direction('down')
            #mytank.move_down()

# store other people's tank  
tanks = {}

cc = Sockclient(tanks)
cc.start()

mycanvas.focus_set()
mycanvas.bind("<Key>",getkey)
mycanvas.pack()

index = 0

while 1:
    index += 1

    if(index%2==0):
        mytank.keep_moving()

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




