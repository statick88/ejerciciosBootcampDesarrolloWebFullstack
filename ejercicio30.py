"""
Crear una clase Empleado con atributos nombre y salario,
Implementar un metodo que calcule el salario anual
"""

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def salario_anual(self):
        return self.salario * 12
    
empleado = Empleado("Diego", 1300)
print(empleado.salario_anual())