import requests
import time
import json
response = requests.get('https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios')
data1 = response.content
cadena = data1.decode()
print(type (cadena))
clientes = cadena.split('{')
print (type(clientes))
print (type(data1))
"""print (clientes)"""

c=0
for caracter in cadena:
	if caracter in "{":
		c=c+1
		cliente = c
		print (c)
		print (cliente)


		