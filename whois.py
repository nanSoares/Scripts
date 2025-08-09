#!/usr/bin/python3

import socket
import sys

    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
s.connect_ex(("whois.iana.org", 43))
s.send((sys.argv[1]+"\r\n").encode('utf-8', errors='replace'))
resp = s.recv(1048).split()
autority = (resp[19]).decode('utf-8', errors='replace')

s.close()

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.settimeout(1)
s1.connect_ex((autority, 43))
s1.send((sys.argv[1]+"\r\n").encode('utf-8', errors='replace'))
resp1 = s1.recv(2048).decode('utf-8', errors='replace')
print(resp1)



