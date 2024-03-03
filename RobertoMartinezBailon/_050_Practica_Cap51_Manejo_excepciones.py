# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap51_Manejo_excepciones 

# try 
auto = "Correcto." # creamos una variable

try: # creamos la excepcion try el cual es un bloque de prueba 
    print(auto) # imprimimos la variable

except: # le decimos que hacer al programa si este no cuenta con una variable de donde tomar los datos
    print("Tu codigo esta mal bro") # imprimimos el resultado 

# Ejemplo mas elaborado 

rein = True  # creamos una variable

while rein: # Creamos un bucle
    try: # Creamos la excepcion try el cual es un bloque de prueba 
        print("Calculadora Basica pero basica lo que le sigue: \n") # imprimimos un texto inicial
        num01 = int(input("Teclea un numero para sumar: ")) # le pedimos al usraio un numero
        num02 = int(input("Introduce un segundo numero para sumarlo al anterior: ")) # le pedimos al usraio un segundo numero
        num03 = int(input("Introduce un tercer numero que se sumara a los dos anteriores: ")) # le pedimos al usraio un tercer numero
    except ValueError: # Creamos una excepcion
        print("No estas tecleando el numero, trucha rey \n") # Imprimimos el resultado de la excepcion
    else: # Creamos un else 
        print("Tu resultado obtenido es: ", num01 + num02 + num03) # imprimimos el resultado del else 
    finally: # creamos un finally
        question = input("¿Deseas seguir sumando numeros S/N:\n") # le pedimos al usuario que tome una decision 
    if question == "N": # establecemos que tiene que poner el usuario para cerrar el programa 
        rein = False 
    else: # creamos otro else 
        print("Tus deseos son ordenes, a seguir sumando \n") # imprimimos el resultado del else 
