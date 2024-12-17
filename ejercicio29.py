"""
Crear una clase vehiculo con atributos marca y modelo,
Crear una clase hija Coche con un atributo adicional velocidad_maxima
"""
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo)
        self.velocidad_maxima = velocidad_maxima

coche = Coche("Kia", "Exportage", 160)
print(coche.marca)
print(coche.velocidad_maxima)