"""
1. Crear una clase basica
Crear una clase llamada Persona con atributos de instancia nombre, edad y correo, 
Implementa un metodo que iprima estos atributos
"""

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

persona = Persona("Juan", 25)
persona1 = Persona("Maria", 30)

persona.mostrar_informacion()
persona1.mostrar_informacion()