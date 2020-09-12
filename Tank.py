import random
import json

class Tank:


 
    def __init__(self, canvas, color='green', init_x=10, init_y=10):
        self.canvas = canvas
        self.id = random.randint(1000,9999)
        self.color = color
        self.pos_x = init_x
        self.pos_y = init_y
        #self.delta_x = 0
        #self.delta_y = 0
        #self.tank_on_canvas = self.canvas.create_rectangle(self.pos_x,self.pos_y,self.pos_x+20,self.pos_y+20,fill=self.color)
        self.speed = 5


    # def update_tank_on_canvas(self):
    #     print(self.delta_x)
    #     print(self.delta_y)
    #     self.canvas.move(self.tank_on_canvas,self.delta_x, self.delta_y)

    def move_to(self, x, y):
        self.pos_x  = x
        self.pos_y  = y
        self.check_wall()
        

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
        #self.delta_y = new_pos_y - self.pos_y
        #self.pos_y = new_pos_y

        if(self.pos_x > 1000 or self.pos_x < 0 ):
            self.pos_x = ( self.pos_x + 1000 ) % 1000
        #self.delta_x = new_pos_x - self.pos_x
        #self.pos_x = new_pos_x


    def status_json(self):
        obj = {"id":self.id,"pos_x":self.pos_x,"pos_y":self.pos_y,"color":self.color}
        return json.dumps(obj)
