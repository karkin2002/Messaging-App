import socket
import pickle

class Network:
    def __init__(self,host,port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.p = self.connect()
    
    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048*8)) # recieveing object, decomposing it
        except:
            pass
    
    def send(self, data): # Send data to server
        try:
            self.client.send(pickle.dumps(data)) # sending object, encrypt it
            return pickle.loads(self.client.recv(2048*8))
    
        except socket.error as e:
            print(e)