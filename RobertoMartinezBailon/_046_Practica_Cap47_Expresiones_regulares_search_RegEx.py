# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap47_Expresiones_regulares_search_RegEx

import re # importas este metodo de busqueda

mensaje = "Que tal, bienvenido al futuro inge " # Imprimes un mensaje de bienvenida

busq = re.search("futuro", mensaje) # Busca un caravter o palabra en especifico

print(busq) # imprimes el resultado
