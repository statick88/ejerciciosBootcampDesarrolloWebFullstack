"""
Crear una clase Tienda que gestione un inventario.
Implementar métodos para agregar, eliminar y mostrar productos.
"""
class Tienda:

    def __init__(self):
        self.invetario = {}

    def agregar(self, producto, cantidad):
        if producto in self.invetario:
            self.invetario[producto] += cantidad
        else:
            self.invetario[producto] = cantidad

    def eliminar(self, producto):
        if producto in self.invetario:
            del self.invetario[producto]
        

    def mostrar_productos(self):
        return self.invetario

tienda = Tienda()
print(tienda.mostrar_productos())
tienda.agregar("manzanas", 10)
print(tienda.mostrar_productos())
tienda.eliminar("manzanas")
print(tienda.mostrar_productos())
