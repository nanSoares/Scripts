#!/usr/bin/python3

#OBS: Sempre ao enviar dados pela rede, enviar como bytes, e nao como ASCII.
#Ao pegar as respostas, decodifica-las para melhor exibicao no output.

import socket 

#Conexao com o servidor

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(("172.16.1.108",21))

#Apos conexao, receber o banner ftp, quantidade em bytes

banner = tcp.recv(1024).decode('utf-8', errors='replace')
print (banner)

#Envia o comando USER e passa o usuario seguido de uma quebra de linha (Enter)
#Recebe 1024 bytes da resposta e armazena no user

tcp.send(b"USER ftp\r\n")
user = tcp.recv(1024).decode('utf-8', errors='replace')
print (user)

tcp.send(b"PASS ftp\r\n")
pw = tcp.recv(1024).decode('utf-8', errors='replace')
print (pw)

tcp.send(b"HELP\r\n")
cmd = tcp.recv(1024).decode('utf-8', errors='replace')
print (cmd)

tcp.send(b"PWD\r\n")
cmd1 = tcp.recv(1024).decode('utf-8', errors='replace')
print (cmd1)
