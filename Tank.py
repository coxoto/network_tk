import random
import json
from datetime import datetime

class Tank:


 

    def __init__(self,id):
        self.id = id
        self.color = 'green'
        self.pos_x = 10
        self.pos_y = 10
        self.total_width = 600
        self.total_height = 600
        self.direction = 'right'
        self.speed = 10

        #self.canvas = canvas
        self.canvas_body = None
        self.canvas_mymark = None
        self.canvas_head = None
        self.net_json = ''
        self.timestamp = 0


    def set_color(self,new_color):
        self.color = new_color

    def random_color(self):
        rand_colors = ['red','green','blue','yellow','orange']
        color_int = random.randint(0,len(rand_colors)-1)
        self.color = rand_colors[color_int]

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
        if(self.pos_y  > self.total_height or  self.pos_y < 0):
            self.pos_y  = ( self.pos_y+self.total_height ) % self.total_height
        if(self.pos_x > self.total_width or self.pos_x < 0 ):
            self.pos_x = ( self.pos_x + self.total_width ) % self.total_width

    def status_json(self):
        obj = {"id":self.id,"pos_x":self.pos_x,"pos_y":self.pos_y,"color":self.color}
        return json.dumps(obj)

    def set_net_json(self,net_json):
        self.net_json = net_json

    def update_canvas(self,canvas,master_id):
        if(self.net_json):
            
            timestamp = int(datetime.timestamp(datetime.now()))
            print(timestamp - self.timestamp)
            if(timestamp - self.timestamp > 1 ):
                canvas.delete(self.canvas_body)
                self.net_json = ''
                return

            tank_data = json.loads(self.net_json)
            if(self.canvas_body):
                for moving_thing in [self.canvas_body,self.canvas_mymark,self.canvas_head]:
                    if(moving_thing):
                        canvas.move(moving_thing,
                            tank_data["pos_x"] - self.pos_x,
                            tank_data["pos_y"] - self.pos_y)
                self.pos_x = tank_data["pos_x"] 
                self.pos_y = tank_data["pos_y"]
                # how to change color here?
            else:
                self.pos_x = tank_data["pos_x"]
                self.pos_y = tank_data["pos_y"]
                self.color = tank_data["color"]
                self.canvas_body = canvas.create_rectangle(
                    self.pos_x,
                    self.pos_y,
                    self.pos_x+20,
                    self.pos_y+20,
                    fill=self.color,tags=self.id)
                if(master_id == self.id):
                    self.canvas_mymark = canvas.create_rectangle(
                        self.pos_x+5,
                        self.pos_y+5,
                        self.pos_x+15,
                        self.pos_y+15,
                        fill='black',tags=self.id)

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp