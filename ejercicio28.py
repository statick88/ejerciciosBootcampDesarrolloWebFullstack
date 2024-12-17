"""
Crear una clase Rectangulo con atributos base y altura
implementar un metodo que determine si es un cuadrado
"""
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def es_cuadrado(self):
        return self.base == self.altura
    
rectangulo = Rectangulo(5, 5)
print(rectangulo.es_cuadrado())
rectangulo1 = Rectangulo(4, 6)
print(rectangulo1.es_cuadrado())