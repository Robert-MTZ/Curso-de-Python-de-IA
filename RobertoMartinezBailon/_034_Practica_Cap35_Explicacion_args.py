# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap35_Explicacion_args

#Ejercicio 01

def autos(*arg): # creamos la funcion
    print("El carro mas vendido es el: " + arg[1] + " y el menos vendido es el: " + arg[7]) # imprimimos solo los ardunetos que queremos

autos("Civic", "Jetta", "Accord", "Typer", "Bocho", "Sentra", "Versa", "Ibiza", "Chevy") # creamos la lista donde se almacenara nuestra informacion


# Ejercicio 02

def camiones_camionetas(camioneta, camion, *arg): # Se crea la funcion
    print("Camioneta: " + camioneta) # se imprime un texto para el contexto
    print("Camion: " + camion) # se imprime un texto para el contexto
    for a in arg: # Se crea un for para crear  una opcion extra
        print("Auto: " + a) # Se imprime la variable creada

lista_autos = ["Ibiza", "Corvette", "Impala", "Sentra", "NSX", "Safari", "Fiesta", "Focus",  "Accord", "Chevy", "Jetta", "Vento", "Passat", "Versa", "Typer", "Charger", "Mustang", "Camaro", "Supra"] # Se crea la lista de donde obtendremos nuestra informacion

camiones_camionetas("Lobo", "Volvo", *lista_autos) # Se imprime el orden de las variables
