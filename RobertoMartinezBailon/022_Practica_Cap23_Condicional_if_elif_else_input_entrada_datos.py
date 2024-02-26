# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap23_Condicional_if_elif_else_input_entrada_datos

aut = int(input('¿Cuantos carros tienes?\n'))
if aut <= 0:
	print('Eres de una clase social humilde.')
elif aut >= 1 and aut <= 3:
	print('Tienes dinero pero no suficiente.')
elif aut > 4 and aut <= 6:
	print('wow eres mirrey.')
elif aut > 7 and aut <= 15:
	print('Eres jodidamente rico.')
elif aut > 16 and aut <= 80:
	print('Te dedicas a algo ilicito.')
else:
	print('no es válido.')
