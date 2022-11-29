import socket
import threading

user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('10.109.89.148', 444)
user.connect(addr)

while True:
    msg = input()
    print(str(msg1, encoding="utf-8"))
    if msg.lower() == "terminate":
        break
    user.send(bytes(msg, encoding='ascii'))
    msg1 = user.recv(1024)
