# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap41_Herencia_clases

class Autos: # creamos una clase para los autos normales
    def __init__(self, modelo, km): # Creamos una funcion donde almacenaremos nuestros datos
        self.modelo = modelo # Creamos un objeto
        self.km = km # Creamos otro objeto
        
    def vista_datos(self): # Creamos una funcion que nos permitira mostrar los datos
        print("El carro es un: " + self.modelo, " y tiene un kilometraje de: ", self.km) # imprimimos resultados

auto1 = Autos("Ferrari", 20000) # le damos valores al objeto 

auto1.vista_datos() # Vemos los datos del objeto

class Autos_premium(Autos): # creamos una clase para los autos premium que heredara las caracteristicas de la clase autos
    pass 

auto2 = Autos_premium("Maclaren", 30000) # damos valores nuevos al objeto 

auto2.vista_datos() # vemos los datos en la consola 
