# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap36_Kwargs

# Ejercicio 1

def autos(**kwargs): # Creamos la funcion
    print("Este carro es un: " + kwargs["auto1"] + " de la marca de Honda") # Imprimimos el resultado mandando llamar la funcion que almacena nuestros datos

autos(auto1="Civic", auto2="Accord", auto3="Typer", auto4="City") # Creamos la lista que sera de donde tomaremos los datos

# Ejercicio 2

def camionetas(camioneta="Ram"): # Creamos la funcion
    print("Mi camioneta es una: " + camioneta) # Imprimimos el reultado mandando llamar a nuestra funcion

camionetas("Lobo")   # Variamos el dato establecido en nuestra funcion
camionetas()         # imprimimos el dato inicial
camionetas("Raptor") # Variamos el dato establecido en nuestra funcion
camionetas()         # imprimimos el dato inicial
camionetas("Ranger") # Variamos el dato establecido en nuestra funcion
