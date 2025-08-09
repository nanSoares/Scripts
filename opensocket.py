#!/usr/bin/python3
import socket
import sys

ip = sys.argv[1]
porta = int(sys.argv[2])

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
response = mysocket.connect_ex((ip,porta))

if (response == 0):
    print("Porta Aberta")
else:
    print("Porta Fechada")

mysocket.close()
