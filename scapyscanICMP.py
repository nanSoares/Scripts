#!/usr/bin/python3

import os
import sys
from scapy.all import *

conf.verb = 0


print ("ICMP SCAN TYPE 08: HOSTS ONLINE")
for ip in range(1,255):
	iprange = f"172.16.0.{ip}"
	pIP = IP(dst=iprange)
	pacote = pIP/ICMP()
	#Redirecionar stderr para /dev/null para ignorar warnings
	with open(os.devnull, 'w') as devnull:
		old_stderr = sys.stderr
		sys.stderr = devnull
	try:
		resp, noresp = sr(pacote,timeout=1)
	finally:
		sys.stderr = old_stderr
		for resposta in resp:
			print (resposta[1].src)
