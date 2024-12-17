"""
Crear una clase Persona con atritutos nombre y edad, telefono, direccion,
Implementar un metodo que devuelva si la persona es mayor de edad
"""
class Persona:

    def __init__(self, nombre, edad, telefono, direccion):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion


    def es_mayor_de_edad(self):
        return self.edad >= 18
    
persona = Persona("Diego", 36, "0992018216", "Quito")
print(persona.es_mayor_de_edad())
print(persona.telefono, persona.direccion)