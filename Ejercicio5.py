# Ejercicio 5: Clase Empleado y Herencia a Gerente 
# Crear una clase Empleado con atributos básicos y luego una clase Gerente que herede y agregue un bono salarial.

import os
os.system("cls")

class Empleado:
    def __init__(self):
        self.nombre = input("ingrese el nombre del empleado: ")
        self.salario = float(input("ingrese el salario del empleado: "))
        
    def mostrar_info(self):
        return print(f"Empleado: {self.nombre}, Salario: {self.salario}")
class Gerente(Empleado):
    def __init__(self):
        super(). __init__()
        self.bono = float(input("Ingrese el bono salarial del gerente: "))
        
    def mostrar_info(self):
        salario_total = self.salario + self.bono
        return print(f"Gerente: {self.nombre}, Salario: {self.salario}, Bono: {self.bono}, Salario Total: {salario_total}")
gerente = Gerente()
gerente.mostrar_info()


