import requests
import json
import mysql.connector
url='https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios' #asigno a una variable la url
conexion1=mysql.connector.connect(host="localhost", user="APIClientes", passwd="jjmLitochaujjm2008*",database="clientes") # Me conecto a la base, luego voy a llamar a la conexion, por ahora la utilizo aqui
mycursor = conexion1.cursor()
data=requests.get(url) #obtengo los datos
#data=response.content #Cargo los datos (son del tipo bytes), esto estaba haciendo mal previamente, llamaba al metodo content y eso no lo podia tratar como JSON
clientes=data.json() #manejo los datos como JSON
for cliente in clientes: #Recorro los clientes para cargarlos en la Base.
	sql = "INSERT INTO cliente (fec_alta,user_name,codigo_zip,credit_card_num,credit_card_ccv,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,fec_birthday,id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	val = (cliente["fec_alta"],cliente["user_name"],cliente["codigo_zip"],cliente["credit_card_num"],cliente["credit_card_ccv"],cliente["cuenta_numero"],cliente["direccion"],cliente["geo_latitud"],cliente["geo_longitud"],cliente["color_favorito"],cliente["foto_dni"],cliente["ip"],cliente["auto"],cliente["auto_modelo"],cliente["auto_tipo"],cliente["auto_color"],cliente["cantidad_compras_realizadas"],cliente["avatar"],cliente["fec_birthday"],cliente["id"])
	mycursor.execute(sql,val) #ejecuto el query
	conexion1.commit() #Hago el commit (hasta que me di cuenta que me faltaba el commit :)
	print(mycursor.rowcount,"record insert")


		
		
		

	








		