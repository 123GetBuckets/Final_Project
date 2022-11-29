import socket
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('10.109.95.251', 444)
user.connect(addr)