# Hacer una calculadora con funciones, el menu tiene 4 opciones, 1 sumar, 2 restar, 3 multiplicar, 4 dividir y 5 salir

print("------ Bienvenido a la Calculadora -----")

def sumar(a,b):
  return f"Resultado: {a + b}"

def restar(a,b):
  return f"Resultado: {a - b}"

def multiplicar(a,b):
  return f"Resultado: {a * b}"

def dividir(a,b):
  return f"Resultado: {a / b}"

def pedir_valores():
  a=float(input("Ingrese el primer numero: "))
  b=float(input("Ingrese el segundo numero: "))
  return a ,b

if __name__ == "__main__":
  while True:
    print(f'''----Menu de Opciones----
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir\n
        Opcio (1-5)
        ''')
    opcion = input("Ingrese una opcion: ")
    
    if opcion == '1':
      a,b = pedir_valores()
      suma = sumar(a,b)
      print(suma)
    elif opcion == '2':
      a,b = pedir_valores()
      resta = restar(a,b)
      print(resta)
    elif opcion == '3':
      a,b = pedir_valores()
      multi = multiplicar(a,b)
      print(multi)
    elif opcion == '4':
      a,b = pedir_valores()
      div = dividir(a,b)
      print(div)
    elif opcion == '5':
      print("Saliendo de la calculadora...")
      break
    else:
      print("Opcion no valida, por favor ingrese una opcion del 1 al 5")

