#!/usr/bin/python3
import socket,sys,re

file = open("lista.txt")
for user in file:
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.connect ((sys.argv[1],25))
	banner = tcp.recv(1024).decode('utf-8', errors='replace')
	tcp.send(b"VRFY "+user.encode())
	res = tcp.recv(1024).decode('utf-8', errors='replace')
	if re.search("252",res):
		print ("Usuario encontrado: "+ res.strip("252 2.0.0"))
	
