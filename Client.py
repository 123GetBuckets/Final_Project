import socket
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('10.109.89.148', 444)
user.connect(addr)

while True:
    msg = input()
    print("\x1B[F\x1B[2K", end="")
    if msg.lower() == "terminate":
        break
    user.send(bytes(msg, encoding='ascii'))

