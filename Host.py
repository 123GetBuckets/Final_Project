import socket
import threading
import time


class host:
    def __init__(self, s_name, HOST, PORT):
        self.name = s_name
        self.HOST = HOST
        self.PORT = PORT
        
    def c_handle(self, conn, c_addr):
        print(f'[CONNECTED]:{c_addr}')
        try:
            while True:
                msg = conn.recv(1024)
                print(f'{c_addr}: {str(msg, encoding="utf-8")}')
                if not msg:
                    break
                for i in self.active:
                    i.send(bytes(f'{c_addr}:{msg}', encoding='ascii'))
        finally:
            self.active.pop(conn)
        conn.close()

    def start(self):
        print(f'[SERVER START]')
        time.sleep(1)
        print(f'--------------')
        time.sleep(3)
        print(f'[SERVER RUNNING]')
        self.name = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = (self.HOST, self.PORT)
        self.name.bind(addr)
        self.name.listen()

        while True:
            conn, c_addr = self.name.accept()
            self.active = []
            self.active.append(conn)
            thread = threading.Thread(target=self.c_handle, args=(conn, c_addr))
            thread.start()
            


server = host("sock", '10.109.89.148', 444)
server.start()
