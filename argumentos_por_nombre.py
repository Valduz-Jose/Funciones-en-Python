print("Argumentos por nombre")

def imprimir_persona(nombre,apellido="",edad=0):
  print(f"Nombre: {nombre} Apellido: {apellido} Edad: {edad}")
  
# llamamos la funcion pasando los argumentod de manera posicional
imprimir_persona("Juan","Perez",30)
# llamamos la funcion pasando los argumentod de manera por nombre
imprimir_persona(nombre="Maria",apellido="Gomez",edad=25)
# se puede intercambiar el orden de esta manera
imprimir_persona(edad=40,apellido="Lopez",nombre="Carlos")

# Argumentos con valores por default
imprimir_persona("Ana") # apellido y edad tomaran los valores por default
imprimir_persona(nombre="Luis",edad=22) # apellido tomara el valor por default