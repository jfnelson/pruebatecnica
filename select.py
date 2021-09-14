import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='prueba')
	try:
		with conexion.cursor() as cursor:
			
			cursor.execute("SELECT * FROM prueba;")
			productos = cursor.fetchall()
			for prueba in proudctos:
				print(productos)
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error no conecta: ", e)