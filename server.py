import threading
import logging
import socket

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)

class SockServer:
    def __init__(self,ip='0.0.0.0',port=999):
        self.addr = (ip , port)
        self.socket = socket.socket()
        self.cliens = {}

    def start(self):
        self.socket.bind(self.addr)
        self.socket.listen()
        threading.Thread(target=self.accept,name='accept').start()

    def accept(self):
        while True:
            s,ip = self.socket.accept()
            logging.info(s)
            logging.info(ip)
            self.cliens[ip] = s
            threading.Thread(target=self.connt,name='connt',args=(s,)).start()

    def connt(self,sockets):

        while True:
            data = sockets.recv(1024)
            logging.info(data)
            del_ks = []
            sockets.send('{}'.format(data.decode('utf8')).encode('utf8'))
            for s in self.cliens.values():
                try:
                    s.send('{}'.format(data.decode('utf8')).encode('utf8'))
                except:
                    logging.info("==============send fail========and close=============")
                    s.close()
                    del_k = list (self.cliens.keys()) [list (self.cliens.values()).index (s)]
                    del_ks.append(del_k)
            for del_k in del_ks:
                del self.cliens[del_k]
                    
    def stop(self):
        for s in self.cliens.values():
                s.close()

        self.socket.close()

cs = SockServer()
cs.start()