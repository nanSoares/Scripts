#!/usr/bin/python3

from urllib.request import urlopen

site = urlopen("https://google.com/")
server = site.info()

print("O servidor Web esta rodando")
print(site.getcode())
print (server['Server'])
print (site.info())
