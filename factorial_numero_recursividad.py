# caso base 0!=1, el factorial de un numero es la multiplicacion de ese numero por el factorial del numero anterior, es decir, n! = n * (n-1)! para n > 0. El caso base es cuando n es igual a 0 o 1, ya que el factorial de ambos numeros es igual a 1 (0! = 1 y 1! = 1). Por lo tanto, la funcion recursiva para calcular el factorial de un numero se puede definir de la siguiente manera:

print("Ejemplo de factorial de un numero con recursividad")

def factorial_recursiva(numero):
  # Caso base 0! = 1 y 1! = 1
  if numero == 0 or numero == 1:
    print(f"Resultado factorial parcial {numero} es: 1")
    return 1
  else:# Caso recursivo
    factorial_parcial = numero * factorial_recursiva(numero - 1)
    print(f"Resultado factorial parcial {numero} es: {factorial_parcial}")
    return factorial_parcial
  
numero = 5
resultado = factorial_recursiva(numero)
print(f"El factorial de {numero} es: {resultado}")