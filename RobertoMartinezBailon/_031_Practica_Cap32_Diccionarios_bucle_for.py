# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap32_Diccionarios_bucle_for

Auto01 = { # Se le asignan valores al diccionario sobre un vehiculo
    "Categoria": "vehiculo",
    "Marca": "Honda",
    "Sub-Marca": "Civic",
    "Precio": "300,000"
    }

Auto02 = { # Se le asignan valores al diccionario sobre un vehiculo
    "Categoria": "vehiculo",
    "Marca": "Honda",
    "Sub-Marca": "Accord",
    "Precio": "340,000"
    }

Auto03 = { # Se le asignan valores al diccionario sobre un vehiculo
    "Categoria": "vehiculo",
    "Marca": "Honda",
    "Sub-Marca": "City",
    "Precio": "280,000"
    }

for c in Auto01: # Se crea un for para imprimir un valor del diccionario
    print(c, "=", Auto01[c] + ".") # Se imprimen los resultados de la seleccion
