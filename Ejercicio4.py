# Ejercicio 4: Clase CuentaBancaria y Herencia a CuentaAhorros
# Crear una clase CuentaBancaria con métodos básicos y luego una clase CuentaAhorros que herede y 
# agregue funcionalidad específica (como interés).

import os 
os.system("cls")    

class CuentaBancaria:
    def __init__(self):
        self.titular = input("Ingrese el nombre del titular de la cuenta: ")
        self.saldo = float(input("Ingrese el saldo inicial de la cuenta: "))
        
    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        
    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")

class CuentaAhorros(CuentaBancaria):
    def __init__(self):
        super().__init__()
        self.tasa_interes = float(input("ingrese la tasa de interés anual (en %): "))
        
    def calcular_interes(self):
        interes = self.saldo * (self.tasa_interes / 100)
        print(f"Interés generado: {interes}")
        return interes

cuenta_ahorros = CuentaAhorros()
cuenta_ahorros.depositar(500)
cuenta_ahorros.retirar(200)
cuenta_ahorros.calcular_interes()
