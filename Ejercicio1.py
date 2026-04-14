# Ejercicio 1: Clase Persona y Herencia a Estudiante
#   Crear una clase Persona con atributos básicos y luego una clase Estudiante que herede de Persona y agregue atributos específicos.
# Resultado:
# Hola, soy Ana y tengo 30 años.
# Hola, soy Luis y tengo 20 años. Estudio Ingeniería.

import os 
os.system("cls")

class Persona:
    def __init__ (self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))
        
class Estudiante(Persona):
    def __init__ (self):
        super(). __init__()
        self.carrera = input("Ingrese su carrera: ")
        
    def mostrar_info(self):
        return print(f"Hola, soy {self.nombre} y tengo {self.edad} años. Estudio {self.carrera}.")
    
a = Estudiante()
a.mostrar_info()
        
