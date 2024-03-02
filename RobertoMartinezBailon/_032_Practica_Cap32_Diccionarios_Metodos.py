# Roberto Martínez Bailón  21310216 Inteligencia Artificial 
# Practica_Cap33_Metodos_diccionarios

auto01 = { # Se crea una lista y se le asignan valores
    'Categoria': "Vehiculo",
    'Marca': "Honda",
    'Sub-Marca': "Civic",
    'Precio': "350,000"
}

auto02 = { # Se crea una segunda lista y se le asignan valores
    "Categoria": "Vehiculo",
    "Marca": "Honda",
    "Sub-Marca": "City",
    "Precio": "230,000"
}

auto03 = { # Se crea una tercer lista y se le asignan valores
    "Categoria": "Vehiculo",
    "Marca": "Honda",
    "Sub-Marca": "Accord",
    "Precio": "280,000"
}

del auto01 # eliminamos completamente la lista de auto01
del auto02["Marca"] # eliminamos solamente marca de la lista
del auto02["Precio"] # eliminamos solo Precio de la lista

print(auto02["Sub-Marca"]) # imprimimos el resultado
 
