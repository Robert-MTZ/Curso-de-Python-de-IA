# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap42_Heredar_propiedades

class Autos: # Se crea una clase la cual sera la que heredara sus datos
    def __init__(self, marca, km): # se crea una funcion donde se almacenen los valores de los objetos
        self.marca = marca # Se crea el primer objeto
        self.km = km # Se crea el segundo objeto

    def vista_datos(self): # Se crea una funcion para que muestre los datos 
        print("El auto es un: " + self.marca, "y tiene un kilometraje de: ", self.km, " Km.") # se imprimen los datos

auto1 = Autos("Ferrari", 40000) # Se le asignan valores a los objetos

auto1.vista_datos() # se ven los datos en la consola

class Autos_premium(Autos): # se crea una clase que heredara los datos de la clase Autos
    def __init__(self, marca, km, color): # se crea una funcion que almacenara los datos de los objetos 
        Autos.__init__(self, marca, km) # se mandan llamar los objetos de la clase autos con el fin de no repetir nombres 
        self.color = color  # se crea un objeto nuevo 

    def vista_datos_premium(self): # se crea una funcion para mostrar los datos
        print("El auto es un: " + self.marca, " con un kilometraje de: ", self.km, "y es de color: ", self.color) # se imprimen los datos

auto2 = Autos_premium("Maclaren", 30000, "Rojo") # Se le asignan valores a los objetos

auto2.vista_datos_premium() # se ven los datos en la consola


        
