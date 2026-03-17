# regresar una tupla de valores
def persona_mayusculas(nombre, apellido,edad):
  print(f"Esta funcion regresa varios valores (tupla)")
  return nombre.upper(), apellido.upper(), edad

# Principal
nombre, apellido, edad = persona_mayusculas("Juan", "Perez", 30)
print(f"Nombre: {nombre} Apellido: {apellido} Edad: {edad}")