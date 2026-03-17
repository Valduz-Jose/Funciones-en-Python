# Es una funcion que se llama a si misma, es decir, una funcion que se invoca a si misma dentro de su propio cuerpo. Las funciones recursivas son una tecnica de programacion que se utiliza para resolver problemas que pueden ser divididos en subproblemas mas pequeños y similares al problema original.
# se debe avanzar poco a poco al caso base, es decir, el caso mas simple que se puede resolver sin necesidad de llamar a la funcion recursiva. Esto es importante para evitar que la funcion se llame a si misma indefinidamente y cause un error de desbordamiento de pila (stack overflow).

print("Ejemplo de funcion recursiva")

def funcion_recursiva(numero):
  if numero == 1:
    print(numero, end = " ")
  else:#Caso recursivo
    funcion_recursiva(numero-1)
    print(numero, end = " ")

# Probamos la funcion
funcion_recursiva(5)