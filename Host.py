import socket 
import threading
import time
address = ('10.109.88.158', 5040)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(address)