import socket
import threading
import asyncio
import INTERFACE
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

INTERFACE.creation("rectangle")

# we need to make it so, if you 
def sending():
    while True:
        try:
            while True:
                msg = input()
                if len(msg) == 0:
                    pass
                if chat_box) != 0:

                else:
                    break

            if msg.lower() == "terminate":
                user.close()
                return False
            user.send(bytes(msg, encoding='ascii'))
        except:
            print("SEND ERROR")
            user.close()
            return False


def rec():
    while True:
        try:
            msg = user.recv(1024)
            if len(msg) == 0:
                return
            print(f'{str(msg, encoding="utf-8")}')
        except:
            print("RECIEVE ERROR")
            user.close()
            return False


def start(IP, PORT):
    addr = (IP, PORT)
    try:
        user.connect(addr)
    except:
        print("Unable to reach HOST")
        return
    thread = threading.Thread(target=rec)
    thread2 = threading.Thread(target=sending)
    thread.start()
    thread2.start()
    return


start('10.109.82.235', 444)
