# usar dos funciones una de grados fahrenheit a celsius y otra de grados celsius a fahrenheit

def celsius_a_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

# Realizo pruebas
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")

fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius")