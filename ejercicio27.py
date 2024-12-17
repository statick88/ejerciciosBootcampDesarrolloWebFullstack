"""
Crear una clase Circulo con atributo radio
Implementar metodos para calcular el area y el perimetro
"""
import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio
    
circulo = Circulo(5)
print(circulo.area())
print(circulo.perimetro())