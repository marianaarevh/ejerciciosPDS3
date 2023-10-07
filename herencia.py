# Arevalo Hernandez Mariana
import math

# EJERCICIOS DE HERENCIA
# Ejercicio 1
print("Ejercicio 1: ")

# Crea una clase padre llamada "Animal" con un atributo "nombre" y un método "hacerSonido()".
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacerSonido(self):
        print(f"{self.nombre} esta haciendo un sonido")

# Luego, crea una subclase llamada "Perro" que herede de "Animal" y agrega un método "ladrido()".
class Perro(Animal):
    def ladrido(self):
        print(f"{self.nombre} es un perro y hace guau guau")


# Crea instancias de ambas clases y muestra cómo se heredan los atributos y métodos de la clase 
# padre a la clase hija.

# Animal
animal1 = Animal("Milo")
animal1.hacerSonido()

# Perro
perro1 = Perro("Maxi")
perro1.hacerSonido()
perro1.ladrido()

print(" ")

# Ejercicio 2
print("Ejercicio 2: ")
# Crea una clase llamada "Figura" con un método "calcularArea()"
class Figura:
    def calcularArea(self):
        print("Se calculó el area de la figura")

# y una subclase llamada "Circulo" que herede de "Figura". 
class Circulo(Figura):

    # Implementa la sobreescritura del método "calcularArea()" en la subclase para calcular el área de un círculo.
    def calcularArea(self, radio):
        area = math.pi * (radio*radio)
        print(f"El area del circulo es de {area}")

# Crea instancias de ambas clases y muestra cómo funciona la sobreescritura de métodos

# Figura
figura1 = Figura()
figura1.calcularArea()

# Circulo
circulo1 = Circulo()
circulo1.calcularArea(10)


