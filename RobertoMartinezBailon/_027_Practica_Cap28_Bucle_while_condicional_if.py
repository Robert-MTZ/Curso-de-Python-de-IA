# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap28_Bucle_while_condicional_if

a = 0 # creamos una variable que inicialize en cero para que nos permita trabajar con nuestro bucle

while a <= 100: # creamos el bucle y establecesmos hasta donde puede llegar 
    a += 5  # establecemos de cuanto sera el incremento

    if a == 20 or a == 40 or a == 70: # estos datos se los saltara en el bucle
        print("Se salto: ", a , "de a") # ponemos un mensaje que nos corrobore que si lo esta haciendo
        continue # el continue es para que a pezar de que se los esta saltando siga con el bucle

    if a == 80 : # con este if se interrumpira el bucle, sin importarle el parametro inicial del bucle
        print("Se interrumpio el bucle cuando se llego al valor de: ", a) # se imprimira este mensaje para corroborar que se este cumpliendo
        break # rompe el flujo de ejecucion del while

    print(a) # imprime todos los demas valores que no cuenten con restricciones 


