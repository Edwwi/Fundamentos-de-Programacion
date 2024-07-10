#2 Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de del arreglo está el mayor número par leído.
lista = []

for contador in range(10):
    pedir = int(input(f"Ingrese el numero #{contador+1}: "))
    lista.append(pedir)

print(f"La lista resultante es: {lista}")
pares = [par for par in lista if par % 2 == 0]
mayor = max(pares)
posicion = pares.index(mayor)

print(f"El numero par mayor esta en la posicion {posicion+1}")