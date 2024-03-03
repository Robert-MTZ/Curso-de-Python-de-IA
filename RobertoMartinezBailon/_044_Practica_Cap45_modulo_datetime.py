# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap45_modulo_datetime

import datetime # Mandamos llamar el modulo datetime para que nos muestre la fecha

date = datetime.datetime.now() # le decimos al modulo que nos imprima los valores actuales en cuanto a la fecha

print("+++++++++++++++++++")
print("Calendar: ") # imprimimos un mensaje que de contexto
print("Year: ", date.year) # imprimimos el año actual
print("Month: ", date.month) # imprimimos el mes actual
print("Day: ", date.day) # imprimimos el dia actual
print("+++++++++++++++++++")
