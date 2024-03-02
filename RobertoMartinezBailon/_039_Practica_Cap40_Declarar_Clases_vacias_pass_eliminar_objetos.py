# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap40_Declarar_clases_vacias_pass_eliminar_objetos

class Autos: # Creamos la clase
    def __init__(self, marca, km): # Creamos la funcion que almacenara los valores de nuestros objetos
        self.marca = marca # creamos donde guardar nuestro objeto
        self.km = km # creamos donde guardar nuestro objeto

    def vista_datos(self): # creamos la funcion que nos imprimira nuestro resultado final
        print("El auto es un: " +  self.marca, self.km) # imprimimos resultado
 
auto1 = Autos("Honda", 78000) # le damos valores a nuestros objetos

print(auto1.marca, auto1.km) # mandamos llamar y imprimimos solo estos objetos

del auto1.km # eliminamos el objeto que almacena el km y tambien puede eliminar objetos completos como auto1
    

