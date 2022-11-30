import socket
import threading

user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('10.109.89.148', 444)
user.connect(addr)


def sending():
    while True:
        msg = input()
        if msg.lower() == "terminate":
            break
        user.send(bytes(msg, encoding='ascii'))


def rec():
    while True:
        msg = user.recv(1024)
        print(str(msg, encoding="utf-8"))


def start():
    thread = threading.Thread(target=sending)
    thread2 = threading.Thread(target=rec)
    thread.start()
    thread2.start()


start()
