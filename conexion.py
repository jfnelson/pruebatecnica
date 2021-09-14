import pymysql
try:
    conexion = pymysql.connect(host='localhost',
     user='root',
      password='',
      db='prueba')
    print("Conexion Exitosa")
except (pymysql.err.OperationalError,pymysql.err.InternationalError) as e:
    print("ocurrio un error no conecta", e)