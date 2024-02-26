# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap25_multiples_condiciones_if

print("Hola amigo, bienvenido al mundo del tunning \n" +
      "¿Que deseas comprar?\n\n"
      + "refacciones disponibles: \n\n" +
      "Rines:\n\n" +
      "1-Rin estilo estrella: 400 dolares.\n" +
      "2-Rin estilo mariposa: 600 dolares.\n\n" +
      "Alerones:\n\n" +
      "3-Aleron de aluminio: 700 dolares.\n" +
      "4-Aleron de fibra de carbono: 1000 dolares.\n\n") 

buy = [3] # Aqui el usario elige la opcion que desea entre el 1 y el 4

money = 1500 # credito inicial

# Declaramos los precios de las refacciones disponibles:
rinEs = 400
rinMar = 600
aleAl = 700
alCab = 1000

if 0 in buy or buy == []:
  print("Escriba el numero corresponidiente a la refaccion que desea, entre el 1 y el 4: ")

if 1 in buy:
    money = money - rinEs

if 2 in buy:
    money = money - rinMar   

if 3 in buy:
    money = money - aleAl

if 4 in buy:
    money = money - alCab

if money < 0:
    print("No te alcanza bro!!!!")

if buy == [1] or buy == [2] or buy == [3] or buy == [4]:
    print("Esto te queda de saldo:"+ str(money)+"dolares")
    print("Se añadieron estas refacciones a tu inventario")
    




    


    
