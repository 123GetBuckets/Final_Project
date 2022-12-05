import socket
import threading
import time


class host:
    def __init__(self, s_name, HOST, PORT):
        self.name = s_name
        self.HOST = HOST
        self.PORT = PORT
        self.active = set()
        self.active_lock = threading.Lock()

    def c_handle(self, conn, c_addr):
        while True:
            try:
                password = conn.recv(1024)
                if str(password, encoding="utf-8") == "JollyGoodShow":
                    conn.send(bytes(f'Welcome! Type [$help] for commands', encoding='ascii'))
                    break
                else:
                    conn.send(bytes('INCORRECT PASSWORD GET OUT', encoding='ascii'))
                    time.sleep(1)
                    conn.close()
                    return
            except:
                pass
        print(f'[CONNECTED]:{c_addr}')
        while True:
            try:
                msg = conn.recv(1024)
                print(f'{c_addr}: {str(msg, encoding="utf-8")}')
                n_msg = (f'\n{c_addr}: {str(msg, encoding="utf-8")}')
                if str(msg, encoding='utf-8') == '$help':
                    conn.send(bytes(
                        f'[$name]: Name Change Prompt\n Type [terminate] (not case sensitive) to disconnect.\n', encoding="ascii"))
                    continue
                elif str(msg, encoding='utf-8') == '$name':
                    name = conn.recv(1024)
                    c_addr = str(name, encoding='utf-8')
                    continue
                elif not msg:
                    break
                with self.active_lock:
                    for i in self.active:
                        if conn != i:
                            i.send(bytes(n_msg, encoding='ascii'))
            except:
                with self.active_lock:
                    self.active.remove(conn)
                    print(f'{c_addr} HAS DISCONNECTED')
                    conn.close()
                    for i in self.active:
                        i.send(bytes(f'{c_addr} HAS DISCONNECTED', encoding='ascii'))
                    return

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
            with self.active_lock:
                self.active.add(conn)
            thread = threading.Thread(target=self.c_handle, args=(conn, c_addr))
            thread.start()


server = host("sock", '10.109.82.235', 444)
server.start()
