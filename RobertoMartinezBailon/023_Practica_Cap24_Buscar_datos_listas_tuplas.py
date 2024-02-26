# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap24_Buscar_datos_listas_tuplas_Phyton

datos = input("Introduce el nombre de un carro:\n ")
carros = ("malibu", "golf", "panamera", "jetta")

if datos in carros[0]:
    print("El auto que elegiste  Malibu esta en la lista")
elif datos in carros[1]:
    print("El auto que elegiste Golf esta en la lista")
elif datos in carros[2]:
    print("El auto que elegiste Panamera esta en la lista")
elif datos in carros[3]:
    print("El auto que elegiste jetta esta en la lista")
else :
    print("El auto que elegiste no se encuentra en nuestra lista")
