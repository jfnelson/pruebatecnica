from pymongo import MongoClient 
from producto import Producto 
from bson.objectid import ObjectId 

def obtener_bd():
    host = "localhost"
    puerto = "27017"
    usuario = "parzibyte"
    palabra_secreta = "hunter2"
    base_de_datos = "prueba"
    cliente = MongoClient("mongodb://{}:{}@{}:{}".format(usuario, palabra_secreta, host, puerto))
    return cliente[base_de_datos]

def insertar(producto):
    base_de_datos = obtener_bd()
    producto = base_de_datos.producto
    return producto.insert_one({
        "nombre": producto.nombre,
        "cantidad": producto.cantidad,
        "precio": producto.precio,
        "detalle":producto.detalle
        
        }).inserted_id

def obtener():
    base_de_datos = obtener_bd()
    return base_de_datos.producto.find()

def actualizar(id, producto):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.producto.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
                "nombre": producto.nombre,
                "cantidad": producto.scantidad,
                "precio": producto.precio,
                "detalle":producto.detalle
                
            }
        })
    return resultado.modified_count

def eliminar(id):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.producto.delete_one(
        {
        '_id': ObjectId(id)
        })
    return resultado.deleted_count


menu = """Bienvenido al Menu para interactuar digita un numero de los que se presentan acontinuacion
1 - Insertar productos
2 - Ver todos los productos
3 - Actualizar todos los productos
4 - Eliminar todos los priductos
5 - Salir
"""
eleccion = None

while eleccion is not 5:
    print(menu)
    eleccion = int(input("Elige: "))
    if eleccion is 1:
        print("Insertar productos")
        nombre = input("Nombre del producto: ")
        cantidad = float(input("Cantidad del producto: "))
        precio = float(input("Precio del producto: "))
        detalle= input("detalle del producto")
        producto = Producto(nombre, cantidad, precio, detalle )
        id = insertar(producto)
        print("El id del producto insertado es: ", id)
    elif eleccion is 2:
        print("Ver todos los  productos...")
        for producto in obtener():
            print("=================")
            print("Id: ", producto["_id"])
            print("Nombre: ", producto["nombre"])
            print("Cantidad: ", producto["cantidad"])
            print("Precio: ", producto["precio"])
            print("detalle",producto["detalle"])
            
    elif eleccion is 3:
        print("Actualizar todos los productos")
        id = input("Proporciona id: ")
        nombre = input("Nuevo nombre del producto: ")
        cantidad = float(input("Nueva cantidad del producto: "))
        precio = float(input("Nuevo precio del producto: "))
        detalle=input("Nuevo detalle del producto")
        producto = Producto(nombre,cantidad, precio, detalle )
        productos_actualizados = actualizar(id, producto)
        print("Cantidad de productos actualizados: ", productos_actualizados)

    elif eleccion is 4:
        print("Eliminar")
        id = input("proporciona el id: ")
        productos_eliminados = eliminar(id)
        print("Cantidad de productos eliminados: ", productos_eliminados)