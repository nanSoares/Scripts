#!/usr/bin/python3

import socket
import sys


if len(sys.argv) < 2:
    print("Utilizacao: {IP}")
else:
    ip = sys.argv[1]

    for porta in range(1,65535):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.settimeout(1)
        res = mysocket.connect_ex((ip,porta))
        if (res == 0):
            print("Porta Aberta: ", porta)
            mysocket.close()
        else:
            mysocket.close()
