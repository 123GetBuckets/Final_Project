import socket
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
addr = ('10.109.95.251', 444)
user.connect(addr)
=======
addr = ('10.109.83.27', 444)
user.connect(addr)

while True:
    msg = input()
    if msg.lower() == "terminate":
        break
    user.send(bytes(msg, encoding='ascii'))

    
>>>>>>> 79e0cb80742d5be53ad8099342fe917e7a7e55b6
