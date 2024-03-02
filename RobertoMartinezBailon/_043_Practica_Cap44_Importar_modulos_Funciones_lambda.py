# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap44_importar_modulos_funciones_lambda

import math # Se importa el modulo math

# Area de un circulo: pi*(rad)2*altura

alt = 3 # declaramos la variable donde se almacenara el valor de la altura

area = lambda rad: round(math.pi * rad * rad * alt, 4) # Utilizamos la funcion lambda para recortar el programa y hacemos la operacion limitando tambien el numero de digitos despues del punto decimal

print(area(12)) # imprimimos el resultado
