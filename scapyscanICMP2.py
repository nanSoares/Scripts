#!/usr/bin/python3

import os
import sys
import logging
from scapy.all import *

# Configurar o Scapy para um modo mais silencioso
conf.verb = 0

# Suprimir warnings configurando o nível de logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

print("ICMP SCAN TYPE 08: HOSTS ONLINE")
for ip in range(1, 255):
    iprange = f"172.16.0.{ip}"
    pIP = IP(dst=iprange)
    pacote = pIP / ICMP()
    resp, noresp = sr(pacote,timeout=1)
    for resposta in resp:
        print(resposta[1].src)
