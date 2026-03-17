# las variables pueden tener un alcance global o local
print("Ejemplo de alcance de variables")

contador_global = 0
def incrementar_contador():
  # Declaramos una variable local
  contador_local = 0
  # Usar la variable global
  global contador_global #si no se indica que es global, se crea una nueva variable local con el mismo nombre
  contador_global += 1
  contador_local += 1
  print(f"Contador global: {contador_global}, Contador local: {contador_local}")
  
# llamamos varias veces la función para ver el efecto en la variable global
incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()

print(f"Valor final del contador global: {contador_global}")