# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap37_Clases_objetos

class Carro(): # Se crea la clase
    peso = 2000    # Se le dan valores
    largo = 176.7  # Se le dan valores
    ancho = 70     # Se le dan valores
    color = "Rojo" # Se le dan valores
    motor = 2.4    # Se le dan valores
    activado = False  # Se le dan valores
    nitro = False  # Se le dan valores
    escape = False  # Se le dan valores
    luces = False  # Se le dan valores
    

    def encender(self): # se crea una funcion para un dato en especifico
         self.activado = True

    def apagar(self): # se crea una funcion para un dato en especifico
         self.activado = False

    def abrir_nitro(self): # se crea una funcion para un dato en especifico
         self.nitro = True

    def cerrar_nitro(self): # se crea una funcion para un dato en especifico
         self.nitro = False

    def abrir_escape(self): # se crea una funcion para un dato en especifico
         self.escape = True

    def cerrar_escape(self): # se crea una funcion para un dato en especifico
         self.escape = False

    def encender_luces(self): # se crea una funcion para un dato en especifico
         self.luces = True

    def apagar_luces(self): # se crea una funcion para un dato en especifico
         self.luces = False

    def estado_nitro(self): # se crea una funcion para un dato en especifico
        if(self.activado):
           return "El nitro esta abierto"
        else:
           return "El nitro esta cerrado"

    def estado_entrada_aire(self): # se crea una funcion para un dato en especifico
        if(self.activado):
           return "La entrada de aire esta abierta"
        else:
           return "La entrada de aire esta cerrada"
        

    def estado_escape(self): # se crea una funcion para un dato en especifico
        if(self.activado):
           return "El escape esta abierto"
        else:
           return "El escape esta cerrado"

    def estado_luces(self): # se crea una funcion para un dato en especifico
        if(self.activado):
           return "Luces prendidas"
        else: 
           return "Luces apagadas"

# Se le dan instrucciones a la clase de lo que se va a imprimir
auto1=Carro() # se le adjudican los datos de la clase

auto1.encender()

auto1.encender_luces()

print(auto1.estado_luces()) # Se imprime el resultado 

auto1.abrir_escape()

print(auto1.estado_escape())  # Se imprime el resultado 

auto1.abrir_nitro()

print(auto1.estado_nitro())  # Se imprime el resultado 









    
