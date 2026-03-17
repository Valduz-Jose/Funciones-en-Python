# Poder comprar snacks, cada uno tiene id y precio , el menu tiene 4 opciones, 1 mostrar snacks (un diccioonario), 2 comprar snack, 3 mostrar ticket, 4 salir

print("------ Bienvenido a la Maquina de Snacks -----")

# Lista de snacks
sancks = [
  {"id":1, "nombre":"Chips", "precio": 1.5},
  {"id":2, "nombre":"Galletas", "precio": 1},
  {"id":3, "nombre":"Sandwuich", "precio": 3}
]

# Lista productos comprados
productos = []

def mostrar_snacks():
  print("------ Snacks Disponibles ------")
  for snack in sancks:
    print(f"ID: {snack['id']}, Nombre: {snack['nombre']}, Precio: {snack['precio']}")

def buscar_snack_por_id(id_snack):
  for snack in sancks:
    if snack['id'] == id_snack:
      return snack
  return None

def comprar_snacks():
  mostrar_snacks()
  id_snack = int(input("Ingrese el ID del snack que desea comprar: "))
  snack_seleccionado = buscar_snack_por_id(id_snack)
  if snack_seleccionado:
    productos.append(snack_seleccionado)
    print(f"Snack comprado: {snack_seleccionado['nombre']}")
  else:
    print("ID de snack no válido.")

def mostrar_ticket():
  print("------ Ticket de Compra ------")
  total = 0
  for producto in productos:
    print(f"Producto: {producto['nombre']}, Precio: {producto['precio']}")
    total += producto['precio']
  print(f"Total a pagar: {total}")

# programa principal
if __name__ == "__main__":
  while True:
    print(f'''----Menu de Opciones----
        1. Mostar Snacks
        2. Comprar Snack
        3. Mostrar Ticket
        4. Salir\n
        Opcio (1-4)
        ''')
    opcion = input("Ingrese una opcion: ")
    if opcion == '1':
      mostrar_snacks()
    elif opcion == '2':
      comprar_snacks()
    elif opcion == '3':
      mostrar_ticket()
    elif opcion == '4':
      print("Saliendo de la maquina de snacks...")
      break
    else:
      print("Opcion no valida, por favor ingrese una opcion del 1 al 4")