import socket

class CondorDecoder:
    
    def __init__(self, udp_ip, udp_port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.socket.bind((udp_ip, udp_port))
    def fetchData(self):
        data, addr = sock.recvfrom(1024)
        self.data = dict(x.split("=") for x in udpstring.split("\n"))
    def getData(self, item):
        return self.data[item]
            
    data = open("condor_data.txt", "r")
    decodeCondorUDP(data.read())