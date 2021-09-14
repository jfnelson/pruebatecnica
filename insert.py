import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='prueba')
	try:
		with conexion.cursor() as cursor:
			consulta = "INSERT INTO productos(id, nombre, cantidad, precio,detalle) VALUES (%s, %s, %s, %s, %s);"
			#insercion de los datos
			cursor.execute(consulta, (" ","mouse", 34, 12.5,"mouse gamer" ))
			cursor.execute(consulta, (" ","teclado", 15, 25.6,"teclado gamer" ))

            
		conexion.commit()
	finally:
		conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error no conecta ", e)