# Argumentos Variables (*args) permiten que una funcion acepte un numero arbitrario de elementos como argumentos. Estos argumentos se pasan a la funcion como una tupla.

print("Ejemplo de Argumentos Variables (*args)")
def superheroe_superpoderes(superheroe, nombre, *args):#args debe ser el ultimo valor en la lista de parametros
    print(f"El superheroe {superheroe} - {nombre} - {args}")
    # iteramos los superpoderes y los imprimimos
    print("Ademas tiene los siguientes superpoderes:")
    for arg in args:
        print(f"- {arg}")
    
superheroe_superpoderes("Superman", "Clark Kent", "Vuelo", "Fuerza", "Visión de Rayos X")
superheroe_superpoderes("Batman", "Bruce Wayne", "Inteligencia", "Habilidades de Combate", "Tecnología Avanzada")
superheroe_superpoderes("Mi Vecino","Juan Perez")
