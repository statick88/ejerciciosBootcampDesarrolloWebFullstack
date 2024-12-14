"""
Clase con Metodos Privados
Crea una clase CuentaBancaria con un metodo privado que 
calcule un interes sobre el saldo
"""

class CuantaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def __calcular_interes(self, tasa):
        return self.saldo * (tasa / 100)
    
    def mostrar_interes(self, tasa):
        print(f"Interes calculado: {self.__calcular_interes(tasa)}")


cuenta = CuantaBancaria(1000)
cuenta.mostrar_interes(5)
cuenta.mostrar_interes(15)