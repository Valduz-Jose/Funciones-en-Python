# *args aguments tupla
# kwargs es un diccionario
# Argumentos Variables con **kwargs permiten que una funcion acepte un numero arbitrario de elementos como argumentos nombrados. Estos argumentos se pasan a la funcion como un diccionario.
def superheroe_superpoderes(nombre,*args,**kwargs):
  print(f"Sperheroe: {nombre} - {args} - Mas info: {kwargs}")
  
# llamamos la funcion
superheroe_superpoderes("Spiderman","Instinto Aracnido",edad=17,empresa="Marvel")
superheroe_superpoderes("Ironman","Armadura","Playboy",edad=45)
superheroe_superpoderes("Mi Vecino",personalidad="Buena Onda")