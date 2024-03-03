# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap48_Expresiones_regulares_findall_RegEx

import re # importamos este metodo de busqueda de caracteres y palabras

mensaje = "Fui a que me revisara el otorrinolaringologo por que me dolia el cuello" # Creamos un mensaje donde nuestro metodo pueda buscar palabras o letras 

search = re.findall("otorrinolaringologo", mensaje) # Buscamos especificamente esta palabra en el mensaje anterior 

print(search) # imprimimos el resultado
