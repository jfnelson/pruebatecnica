
import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='prueba')
	try:
		with conexion.cursor() as cursor:
			
			consulta = "DELETE FROM productos WHERE id= %s;"
			id = 3
			cursor.execute(consulta, (id))
 
		# Hacer commit a la base de datos para guardar cambios
		conexion.commit()
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error no conecta: ", e)