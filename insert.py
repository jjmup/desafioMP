import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="APIClientes", passwd="jjmLitochaujjm2008*",database="clientes")
cursor1=conexion1.cursor()
sql="insert into cliente(id) values ('3')"


cursor1.execute(sql)
conexion1.commit()
conexion1.close()