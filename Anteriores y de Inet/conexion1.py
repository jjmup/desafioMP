import mysql.connector
import time
 

conexion1=mysql.connector.connect(host="localhost", user="APIClientes", passwd="jjmLitochaujjm2008*")
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:

    print(base)

conexion1.close()
time.sleep(15)