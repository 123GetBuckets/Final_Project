import socket 
import threading
import time
address = ('10.109.88.158', 444)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(address)

sock.listen(10)
client, addr = sock.accept()
print(f'{client} has connected')