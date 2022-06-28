# En este segundo ejercicio, tendreis que crear un archivo py y dentro creareis una clase Vehiculo,
# hareis un objeto de ella, lo guardareis en un archivo y luego lo cargamos.

import pickle


def abre_fichero(nombre_fichero, tipo):
    """
    Funcion que crea o lee un archivo en funcion del tipo ('w', 'wb', 'r', 'rb'...)
    """
    return open(nombre_fichero, tipo)


class Vehiculo:
    tipo_motor = ""
    numero_ruedas = 0
    velocidad = 0.0

    def __init__(self, tipo_motor, numero_ruedas, velocidad):
        self.tipo_motor = tipo_motor
        self.numero_ruedas = numero_ruedas
        self.velocidad = velocidad

    def __str__(self):  # Salida informal de texto, Video sesion 8
        text = f'Tipo de motor: {self.tipo_motor}\nNumero de ruedas: {self.numero_ruedas}\nVelocidad: {self.velocidad}\n'
        return text

    def __repr__(self):  # Salida tecnica de texto, representacion en forma de string del objeto, Video sesion 8
        repres = f'Motor: {self.tipo_motor}\n#N ruedas: {self.numero_ruedas}\nKm/h: {self.velocidad}\n'
        return repres


vehiculo_1 = Vehiculo("Diesel", 4, 120.5)
# print(str(vehiculo_1)) Para probar ambos metodos de salida de texto vistos en clase
# print(repr(vehiculo_1))

archivo = abre_fichero('datos_vehiculo.bin', 'wb')  # Se crea el archivo dandole nombre e introduciendo el tipo 'wb'
pickle.dump(vehiculo_1, archivo)
archivo.close()

# Obtener datos del objeto que hemos creado (vehiculo_1)

archivo_ejemplo_1 = abre_fichero('datos_vehiculo.bin', 'rb')  # Se lee el archivo introduciendo el tipo 'rb'
vehiculo_ejemplo_1 = pickle.load(archivo_ejemplo_1)
archivo_ejemplo_1.close()

print(type(vehiculo_ejemplo_1))
print(str(vehiculo_ejemplo_1))
print(repr(vehiculo_ejemplo_1))
