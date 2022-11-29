import socket
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('10.109.83.27', 444)
user.connect(addr)

while True:
    msg = input()
    if msg.lower() == "terminate":
        break
    user.send(bytes(msg, encoding='ascii'))

    