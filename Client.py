import socket
import getpass
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('10.109.95.251', 444)
user.connect(addr)

while True:
    msg = getpass.getpass()
    if msg.lower() == "terminate":
        break
    user.send(bytes(msg, encoding='ascii'))

