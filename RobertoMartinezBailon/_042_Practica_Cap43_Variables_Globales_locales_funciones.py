# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap43_Variables_Globales_locales_funciones 

car1 = "Civic" # Creamos una variable fuera de la funcion lo cual la hace variable global

def Autos(): # Creamos una funcion que almacenara una variable
    global car1 # creamos una variable global dentro de la funcion
    car1 = "Accord" # Cambiamos el valor de la variable 

Autos() # mandamos llamar a la funcion

print(car1) # imprimimos el resultado 
    
