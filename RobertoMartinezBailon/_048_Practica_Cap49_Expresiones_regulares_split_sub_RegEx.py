# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap49_Expresiones_regulares_split_sub_RegEx

# split()

import re # mandamos llamar este metodo de busqueda de palabras o letras

mensaje = "El Arte es la evidencia de que vivimos en este planeta" # le damos el mensaje con el que va a trabajar 

res = re.split(" ", mensaje, 5) # Nos sepsrara el mensaje por medio de comas ("numero o letra que se busca", texto de donde se esta sacando la informacion, limitaciones de busqueda) ejemplo: -> ("e", mensaje, 3)

print(res) # Nos imprimira el resultado

# sub()

mensaje1 = "Cuando todo parezca ir en contra tuyo, recuerda que el avión despega con el viento en contra, no a favor. – Henry Ford" # le damos material con el cual trabajar al metodo

res1 = re.sub(" ", "+++", mensaje1, 6) # sirve para sustituir lo que se busca por algun caracter

print(res1) # se imprime el resulktado final
