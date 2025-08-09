#!/usr/bin/python3

import socket
import sys

ip = input("Digite o IP: ")
porta = int(input("Digite a Porta: "))

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect_ex((ip,porta))
banner = mysocket.recv(1024)
print (banner)
