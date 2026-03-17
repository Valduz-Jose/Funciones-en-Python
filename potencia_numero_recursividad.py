# Calcular la potencia d eun numero con recursividad, la potencia de un numero se define como el resultado de multiplicar ese numero por si mismo un cierto numero de veces. Por ejemplo, 2 elevado a la potencia de 3 (2^3) es igual a 2 * 2 * 2 = 8. La funcion recursiva para calcular la potencia de un numero se puede definir de la siguiente manera:

print("Ejemplo de potencia de un numero con recursividad")

def potencia_recursiva(base,exponente):
  # Caso base: cualquier numero elevado a la potencia de 0 es igual a 1
  if exponente == 0:
    print(f"Resultado potencia parcial {base}^{exponente} es: 1")
    return 1
  else:# Caso recursivo
    potencia_parcial = base * potencia_recursiva(base, exponente - 1)
    print(f"Resultado potencia parcial {base}^{exponente} es: {potencia_parcial}")
    return potencia_parcial

# Probamos la funcion
base = 2
exponente = 3
resultado = potencia_recursiva(base, exponente)
print(f"El resultado de {base}^{exponente} es: {resultado}")