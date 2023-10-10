# Arevalo Hernandez Mariana
import math

# EJERCICIOS DE POLIMORFISMO

# Ejercicio 1
print("Ejercicio 1: ")

# Crea una clase llamada "Figura" con un método "calcularArea()" que devuelve un valor predeterminado, como 0.
class Figura:
    def calcularArea(self):
        return 0

# Luego, crea subclases llamadas "Circulo" y "Rectangulo" que hereden de "Figura". 
# En estas subclases, sobreescríbe el método "calcularArea()" para calcular el área específica de cada figura. 
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcularArea(self):
        area = math.pi * self.radio ** 2
        return area

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        area = self.base * self.altura
        return area

# Luego, crea instancias de ambas subclases y llama al método "calcularArea()" en cada una.
circulo = Circulo(10)
rectangulo = Rectangulo(6, 10)

areaCirculo = circulo.calcularArea()
areaRectangulo = rectangulo.calcularArea()

print("Área círculo = ", areaCirculo)
print("Área rectángulo = ", areaRectangulo)

print(" ")

# Ejercicio 2
print("Ejercicio 2: ")

# Crea una clase llamada "Fruta" con un método "obtenerColor()" que devuelve un color predeterminado, como "desconocido". 
class Fruta:
    def obtenerColor(self):
        return "desconocido"

# Luego, crea subclases llamadas "Manzana" y "Banana" que hereden de "Fruta". 
class Manzana(Fruta):
    def obtenerColor(self):
        return "rojo"

class Banana(Fruta):
    def obtenerColor(self):
        return "amarillo"

# En el programa principal, declara una variable de tipo "Fruta" y asígnale instancias de "Manzana" y "Banana". 
fruta1 = Manzana()
fruta2 = Banana()

# Llama al método "obtenerColor()" en ambas instancias y muestra el color de cada fruta. 
colorFruta1 = fruta1.obtenerColor()
colorFruta2 = fruta2.obtenerColor()

print("Color Manzana:", colorFruta1)
print("Color Banana:", colorFruta2)

print(" ")

# Ejercicio 3
print("Ejercicio 3: ")

# Crea una clase llamada "Animal" con un método "mover()" que imprima el movimiento genérico, como "volar" o “nadar”. 
class Animal:
    def mover(self):
        return ("movimiento generico")

# Luego, crea subclases llamadas "Perro",  "Pez" y “Pájaro” que hereden de "Animal". 
class Perro(Animal):
    def mover(self):
        return ("caminar")

class Pez(Animal):
    def mover(self):
        return ("nadar")

class Pajaro(Animal):
    def mover(self):
        return ("volar")

# Crea instancias de ambas subclases y llama al método "mover()" en cada una.
perro = Perro()
pez = Pez()
pajaro = Pajaro()

# En las subclases, sobreescríbe el método "mover()" para imprimir el movimiento específico para cada animal. 
print("Perro: ", perro.mover())
print("Pez: ", pez.mover())
print("Pájaro: ", pajaro.mover())