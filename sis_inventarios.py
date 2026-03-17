# Sistema de inventarios: crear un sistema con un menu, mostrar inventario, agregar producto, buscar producto y salir

print("Bienvenido al sistema de inventarios")

inventario = [
    {'id': 1, 'nombre':'Camisa', 'cantidad': 10, 'precio': 20.0},
    {'id': 2, 'nombre':'Pantalones', 'cantidad': 10, 'precio': 20.0},
    {'id': 3, 'nombre':'Zapatos', 'cantidad': 10, 'precio': 20.0},
]

def mostrar_inventario():
  print("------ Inventario ------")
  for producto in inventario:
    print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")

def agregar_producto():
  print("Agregar Producto")
  id_producto = int(input("Ingrese el ID del producto: "))
  nombre_producto = input("Ingrese el nombre del producto: ")
  cantidad_producto = int(input("Ingrese la cantidad del producto: "))
  precio_producto = float(input("Ingrese el precio del producto: "))
  nuevo_producto = {'id': id_producto, 'nombre': nombre_producto, 'cantidad': cantidad_producto, 'precio': precio_producto}
  inventario.append(nuevo_producto)
  print(f"Producto {nombre_producto} agregado al inventario")
  
def buscar_producto():
  print("Buscar Producto")
  id_producto = int(input("Ingrese el ID del producto a buscar: "))
  for producto in inventario:
    if producto['id'] == id_producto:
      print(f"Producto encontrado: ID: {producto['id']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
      return
  print("Producto no encontrado")
  
  
if __name__ == "__main__":
  while True:
    print(f'''----Menu de Opciones----
        1. Mostar Inventario
        2. Agregar Producto
        3. Buscar Producto
        4. Salir\n
        Opcio (1-4)
        ''')
    opcion = input("Ingrese una opcion: ")
    if opcion == '1':
      mostrar_inventario()
    elif opcion == '2':
      agregar_producto()
    elif opcion == '3':
      buscar_producto()
    elif opcion == '4':
      print("Saliendo del sistema de inventarios...")
      break
    else:
      print("Opcion no valida, por favor ingrese una opcion del 1 al 4")