import socket
import threading
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def sending():
    while True:
        msg = input()
        if msg.lower() == "terminate":
            break
        user.send(bytes(msg, encoding='ascii'))

    user.close()
def rec():
    while True:
        msg = user.recv(1024)
        print(f'{str(msg, encoding="utf-8")}')


def start(IP, PORT):
    addr = (IP, PORT)
    user.connect(addr)
    thread = threading.Thread(target=sending)
    thread2 = threading.Thread(target=rec)
    thread.start()
    thread2.start()

start('10.109.81.174', 444)