print("Numero es par")

def es_par(numero):
  if numero % 2 == 0:
    return True
  else:
    return False
# Probamos la funcion
if __name__ == "__main__":
  numero = int(input("Ingrese un numero: "))
  if es_par(numero):
    print(f"El numero {numero} es par.")
  else:
    print(f"El numero {numero} es impar.")