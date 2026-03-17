# Proporciona el pago sin impuesto,monto de impuesto y se calcula el pago con impuesto

# Funcion q calcula el total de un pago incluyendo el impuesto

def calcular_total_pago(pago_sin_impuesto, impuesto):
  pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
  return pago_total


# Programa principal
pago_sin_impuesto = float(input("Ingrese el pago sin impuesto: "))
impuesto = float(input("Ingrese el porcentaje de impuesto: "))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f"El pago total con impuesto es: {pago_con_impuesto}")