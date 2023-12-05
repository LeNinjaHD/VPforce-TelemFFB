import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 31090
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


data, addr = sock.recvfrom(4096) # buffer size is 1024 bytes

print(data)