# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap38_

class autos(): # Se crea la clase

    def __init__(self, nombre, color): # Se crea la funcion utilizando el metodo init
        self.nombre = nombre
        self.color = color

    def sal(self): # Se crea la funcion que se activara cual el carro llegue
        print("Tu carro es un: " + self.nombre + " de color: " + self.color + " por lo tanto te informamos que ya se encuentra verificado")

    def exit(self): # Se crea la funcion que se activara cuando el carro se valla 
        print("El carro: " + self.nombre + " esta aprovado, ya puedes irte ")

# se le asignan valores a la s variables
auto1=autos("Accord", "Blanco") 

auto2=autos("Civic", "Rojo")

auto3=autos("Jetta", "Amarillo")

# se les da el orden de impresion deseado 
auto1.sal()
auto2.sal()
auto3.sal()
auto1.exit()
auto2.exit()
auto3.exit() 
