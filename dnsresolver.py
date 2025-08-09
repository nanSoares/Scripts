#!/usr/bin/python3

import socket
import sys

host = sys.argv[1]

print (host, "-->", socket.gethostbyname(host))
