# En este ejercicio, tendréis que crear un archivo py donde creeis un archivo txt,
# lo abrais y escribais dentro del archivo. Para ello, tendreis que acceder dos veces al archivo creado.

# Programa que escribe un archivo con el nombre de varias calles de un listado de direcciones dado,
# en el que se ignoran las avenidas

def escribir(nombre_fichero, datos): # Crea y escribe en el archivo
    archivo = open(nombre_fichero, 'w')

    for linea in datos:
        if linea.lower().startswith('av'):  # Si la direccion es una avenida la ignora
            continue
        else:
            linea = linea.lower().replace("calle", '').replace("c/", '')  # Solo escribe el nombre
            nombre_calles = " ".join(linea.split()).title() + '\n'  # Quita los espacios, vuelve a poner
            # la primera letra en mayuscula y hace un salto

        archivo.write(nombre_calles)

    archivo.close()

lista_direcciones = [
    'Avenida La Paz',
    'Calle Arces',
    'Av. Juan Ramon',
    'C/ Robles',
    'Calle Saucos',
    'Calle Encinas'
]

escribir('calles.txt', lista_direcciones)