import socket
import time
import subprocess
import sys



breacher = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    for i in range(1, 65535):
        port = i
        addr = ('129.32.224.91', port)
        x = breacher.connect_ex(addr)
        if x == 0:
            print(port, " is open")
        breacher.close()
except socket.error:
    sys.exit()
except socket.gaierror:
    sys.exit()
