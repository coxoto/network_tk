import threading
import socket
import logging
#import datetime
import json
from Tank import Tank
from datetime import datetime

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)


class Sockclient:
    def __init__(self,tanks,ip='10.10.10.100',port=999):
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
            # jsondata = '{}'.format(data.strip())
            # logging.info(jsondata)
            net_json_data = str(data.strip(),'utf-8')
            jsonobj = None
            try:
                jsonobj = json.loads(net_json_data)
            except:
                logging.info("net_json_wrong")
            if(jsonobj):
                if(not self.tanks.get(jsonobj['id'])):
                    self.tanks[jsonobj['id']] = Tank(jsonobj['id'])
                self.tanks[jsonobj['id']].set_net_json(net_json_data)
                timestamp = int(datetime.timestamp(datetime.now()))
                self.tanks[jsonobj['id']].set_timestamp(timestamp)
      
    def send(self,message:str):
        data = '{}\n'.format(message.strip()).encode()
        self.clients.send(data)

    def stop(self):
        self.event.set()
        self.clients.close()



