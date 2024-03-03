# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap50_Secuencias_especiales_metacaracteres_sets

import re # Se crea un modulo re o se manda llamar 

# metacarcteres

mensaje = ("Los retos son regalos que nos obligan a buscar un nuevo centro de gravedad. No luches contra ellos. Simplemente encuentra una nueva forma de mantenerte en pie. - Oprah Winfrey") # se crea un texto de donde se van a extrae los datos

res = re.findall("reg..os|obli..n|gra...ad", mensaje) # se utiliza el findall para buscar palabras o caracteres especificos

print(res) # se imprime el resultado 

# sets

mensaje1 = ("El acto más valiente sigue siendo pensar por uno mismo. En voz alta. - Coco Chanel") # se crea un mesaje de donde se van a extraer los datos  

res1 = re.findall("[a-g]", mensaje1) # se utiliza 

print(res1) # se imprime el resultado final
