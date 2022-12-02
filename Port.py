import socket
import time
import subprocess
import sys



breacher = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    for port in range(1, 300):
        # print(port)
        addr = ('207.244.91.154', port)
        x = breacher.connect_ex(addr)
        if x == 0:
            print(port, " is open")
        breacher.close()
except socket.error:
    sys.exit()
except socket.gaierror:
    sys.exit()
