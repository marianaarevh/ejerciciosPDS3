#EJERCICIOS DE HERENCIA

#Ejercicio 1

#Crea una clase padre llamada "Animal" con un atributo "nombre" y un método "hacerSonido()".
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacerSonido(self):
        print(f"{self.nombre} esta haciendo un sonido")

#Luego, crea una subclase llamada "Perro" que herede de "Animal" y agrega un método "ladrido()".
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

