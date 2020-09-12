import random
import json

class Tank:


 
    def __init__(self, color='green', init_x=10, init_y=10):
        self.id = random.randint(1000,9999)
        self.color = color
        self.pos_x = init_x
        self.pos_y = init_y
        self.direction = 'right'
        self.speed = 10

    def set_color(self,new_color):
        self.color = new_color


    def move_to(self, x, y):
        self.pos_x  = x
        self.pos_y  = y
        self.check_wall()

    def set_direction(self,new_direction):
        self.direction = new_direction
        
    def keep_moving(self):
        if(self.direction == 'right'):
            self.move_right()
        if(self.direction == 'left'):
            self.move_left()
        if(self.direction == 'up'):
            self.move_up()
        if(self.direction == 'down'):
            self.move_down()


    def move_right(self):
        self.pos_x += self.speed
        self.check_wall()

    def move_left(self):
        self.pos_x -= self.speed
        self.check_wall()
        
    def move_up(self):
        self.pos_y -= self.speed
        self.check_wall()
        
    def move_down(self):
        self.pos_y += self.speed
        self.check_wall()
    
    def check_wall(self):
        if(self.pos_y  > 800 or  self.pos_y < 0):
            self.pos_y  = ( self.pos_y+800 ) % 800
        if(self.pos_x > 1000 or self.pos_x < 0 ):
            self.pos_x = ( self.pos_x + 1000 ) % 1000


    def status_json(self):
        obj = {"id":self.id,"pos_x":self.pos_x,"pos_y":self.pos_y,"color":self.color}
        return json.dumps(obj)
