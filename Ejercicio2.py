# Ejercicio 2: Clase Vehículo y Herencia a Automóvil
# Crear una clase Vehículo con atributos genéricos y luego una clase Automóvil que herede de Vehículo y agregue atributos específicos.
# Resultado:
#   Vehículo: Toyota Corolla
#   Vehículo: Ford Mustang, Tipo: Deportivo

import os
os.system("cls")

class Vehiculo:
        def __init__ (self):
            self.marca = input("Ingrese la marca del vehículo: ")
            self.modelo = input("Ingrese el modelo del vehículo: ")
            
        def mostrar_vehiculo(self):
            return print(f"Vehículo: {self.marca} {self.modelo}")
            
class Automovil(Vehiculo):
        def __init__ (self):
            super(). __init__()
            self.tipo = input("Ingrese el tipo de automóvil (deportivo, sedán, coupe, etc): ")
            
        def mostrar_tipo(self):
            return print(f"Vehículo: {self.marca} {self.modelo}, Tipo: {self.tipo}.")
        
a = Automovil() 
a.mostrar_tipo()

b = Vehiculo()
b.mostrar_vehiculo()