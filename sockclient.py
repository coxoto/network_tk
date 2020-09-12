import threading
import socket
import logging
import datetime
import json


FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)


class Sockclient:
    def __init__(self,tanks,ip='127.0.0.1',port=999):
        self.clients = socket.socket()
        self.raddr = (ip,port)
        self.event = threading.Event()
        #self.mycanvas = mycanvas
        #self.root = root
        self.tanks = tanks


    def start(self):
        self.clients.connect(self.raddr)
        self.send('I am new, I am online')
        threading.Thread(target=self.recive,name='receive').start()


    def recive(self):
        while not self.event.is_set():
            data = self.clients.recv(1024)
            # logging.info(data)
            if data.strip() == b'quit':
                break
            #message = '{:%Y/%m/%d %H:%M:%S}{}:{}\n{}\n'.format(datetime.datetime.now(),*self.raddr,data.strip())
            #logging.info(message)
            jsondata = '{}'.format(data.strip())
            logging.info(jsondata)
            try:
                jsonobj = json.loads(str(data.strip(),'utf-8'))
                #logging.info(jsonobj['id'])
                if(self.tanks.get(jsonobj['id'])):
                    #logging.info("=====> old tank")
                    self.tanks[jsonobj['id']]["delta_x"] = jsonobj['pos_x'] - self.tanks[jsonobj['id']]['pos_x']
                    self.tanks[jsonobj['id']]["delta_y"] = jsonobj['pos_y'] - self.tanks[jsonobj['id']]['pos_y']
                else:
                    #logging.info("=====> new tank")
                    self.tanks[jsonobj['id']] = jsonobj
                    self.tanks[jsonobj['id']]["delta_x"] = 0
                    self.tanks[jsonobj['id']]["delta_y"] = 0
                    
                    #logging.info(self.tanks)
                
            except:
                logging.info("*****!!!!!!!!!!!!!*****")

      


    def send(self,message:str):
        data = '{}\n'.format(message.strip()).encode()
        self.clients.send(data)

    def stop(self):
        self.event.set()
        self.clients.close()



