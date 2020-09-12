from sockclient import Sockclient
from tkinter import *
import random
import time
from Tank import Tank
import platform


root = Tk()
mycanvas = Canvas(root,width=600,height=600,bg="black")

my_id = random.randint(1000,9999)
mytank = Tank(my_id)
mytank.random_color()
# store other people's tank  
tanks = {}


def getkey(event):
    #right 
    if(platform.system() == 'Windows'):

        if(event.keysym == "d"):
            mytank.set_direction('right')
            #mytank.move_right()
            
        #left
        if(event.keysym == "a"):
            mytank.set_direction('left')
            #mytank.move_left()
        
        #up
        if(event.keysym == "w"):
            mytank.set_direction('up')
            #mytank.move_up()

        #down
        if(event.keysym == "s"):
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


cc = Sockclient(tanks)
cc.start()
mycanvas.focus_set()
mycanvas.bind("<Key>",getkey)
mycanvas.pack()


while True:

    mytank.keep_moving()
    cc.send(mytank.status_json())
    draw_tanks = tanks.copy()
    for t in draw_tanks.values():
        t.update_canvas(mycanvas,my_id)
    
    root.update()
    time.sleep(0.1)





