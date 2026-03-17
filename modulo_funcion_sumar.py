def sumar(a,b):
  resultado = a + b
  return resultado

# Prueba funcion sumar
if __name__ == "__main__":# Esto se ejecuta solo si se ejecuta este archivo directamente, no se ejecuta si se importa como modulo
  sumar(15,30)
  print(f'Prueba de la funcion sumar: {sumar(15,30)}')