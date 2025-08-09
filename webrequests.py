#!/usr/bin/python3

import requests

site = requests.get("http://terra.com.br/")
status = site.status_code

if (status == 200):
    print ("Pagina Existe")
    print(site.content)
else:
    print("Pagina Inexistente")
