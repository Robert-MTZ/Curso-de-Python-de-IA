# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap39_self_Poo

class Carros: # Creamos la clase
    def __init__(self, marca, km, color): # definimos nuestras variables en una funcion
        self.marca = marca # se define donde se almacenara el dato de marca
        self.km = km # se define donde se almacenara el dato de km
        self.color = color # se define donde se almacenara el dato de color

    def vista_datos(self): # Creamos una funcion para que nos muestre los datos almacenados
        print("la marca del carro es un: " + self.marca, self.km, self.color)  # Creamos un print para que nos muestre sus datos

auto1 = Carros("Ford", 123, "Rojo") # le damos valores a nuestras variables
auto1.vista_datos() # mostramos datos

auto1.km = 154 # cambiamos el valor de nuestra variable elegida
auto1.vista_datos() # mostramos el cambio
