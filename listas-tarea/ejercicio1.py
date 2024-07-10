#1 Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído.
lista = []

for contador in range(10):
    pedir = int(input(f"Ingrese el numero #{contador+1}: "))
    lista.append(pedir)

print(f"La lista resultante es: {lista}")

mayor = max(lista)
posicion = lista.index(mayor)

print(f"El numero mayor esta en la posicion {posicion+1}")