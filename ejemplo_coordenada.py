print("Obtener coordenadas x,y,z")

def obtener_coordenadas():
  x,y,z = 10,20,30
  return x,y,z

resultado = obtener_coordenadas()
print(f"Coordenadas: {resultado}")

# unpacking de la tupla
x1,y1,z1 = resultado
print(f"Coordenadas unpacking: x={x1} y={y1} z={z1}")