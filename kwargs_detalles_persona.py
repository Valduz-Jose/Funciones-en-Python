print("Imprimir detalles de una persona con **kwargs")

def imprimir_detalle_persona(**kwargs):
  print("\nValores recibidos: ")
  for llave, valor in kwargs.items():
    print(f"{llave}: {valor}")
    
# llamamos la funcion
imprimir_detalle_persona(nombre="Juan", edad=30, profesion="Ingeniero")
imprimir_detalle_persona(nombre="Maria", edad=25, profesion="Diseñadora", ciudad="Madrid")
imprimir_detalle_persona()
