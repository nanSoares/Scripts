#!/usr/bin/python3

import socket,sys

if len(sys.argv) !=3:
	print ("Modo de uso: python smtpenum.py IP User")
	sys.exit(0)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1],25))
banner = tcp.recv(1024).decode('utf-8', errors='replace')
print (banner)

tcp.send(b"VRFY "+sys.argv[2].encode() + b"\r\n")
user = tcp.recv(1024).decode('utf-8', errors='replace')
print (user)


