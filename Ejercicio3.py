# Ejercicio 3: Clase Animal y Herencia a Perro y Resultado 
# Depósito de $500. Saldo actual: $1500
# Interés aplicado: $75.00. Saldo actual: $1575.00
# Retiro de $200. Saldo actual: $1375
# Gato:
# Crear una clase base Animal con un método genérico, y luego dos clases derivadas (Perro y Gato) que hereden y
# personalicen el comportamiento.

import os   
os.system("cls")

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hacer_sonido(self):
        return "El animal hace un sonido genérico."
class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Guau!"
class Gato(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Miau!"
perro = Perro("rex")
gato = Gato("mimi")

print(perro.hacer_sonido())
print(gato.hacer_sonido())
