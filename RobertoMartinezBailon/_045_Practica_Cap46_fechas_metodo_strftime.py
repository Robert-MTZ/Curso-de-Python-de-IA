# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap46_fechas_metodo_strftime

import datetime, locale # se mandan llamar datetime para las fechas y locale para el idioma con el que se esta trabajando

locale.setlocale(locale.LC_ALL, "es-ES") # se hace esta linea para trabajar con los resultados en español

date = datetime.datetime.now() # se trabaja con datetime para trabajar con las fechas

print(date.strftime("%c")) # se imprime el resultado del modulo
