import requests
import re
import json
response=requests.get('https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios')
data1=response.content #Cargo los datos (son del tipo bytes)
cadena=data1.decode() #paso a string
separador='{' #defino el separador del string para pasarlo a lista
#cadena_de_clientes=re.sub("}","",cadena) #no me funciona para borrar la "}"
#cadena_de_clientes=cadena.replace("}",",") #no me funciona para borrar la "}"
clientes = cadena.split(separador) #separo el string segun el separador (la idea es separar cada cliente)
c=0
for cliente in clientes:
	c=c+1
	nombre='Cliente'+ str (c-1)
	print (nombre)
	print (cliente)
	#cliente_json=clientes
	#json.dumps(cliente_json)
	#usuario=cliente_json['user_name']
	#print (usuario)
	"""for el_cliente in nombre:
		json.dumps()
		print (cliente_json['fec_alta'])"""




		