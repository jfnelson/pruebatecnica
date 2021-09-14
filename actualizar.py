import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='prueba')
	try:
		with conexion.cursor() as cursor:
			
			consulta = "UPDATE productos SET nombre = %s, cantidad =%s, precio=%s, detalle=%s WHERE id = %s;"
			nuevo_nombre = "MouseGamerXR"
			nueva_cantidad = 25
			nuevo_precio = 12.75
			nuevo_detalle = "MouseRGB"

			id_editar = 1
			cursor.execute(consulta, (nuevo_nombre, nueva_cantidad, nuevo_precio, nuevo_detalle, id_editar))
 
		# hacer commit para guardar los cambios en la base de datos
		conexion.commit()
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error no conecta: ", e)