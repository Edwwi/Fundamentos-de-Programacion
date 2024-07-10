# Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído.
lista = []

for contador in range(10):
    pedir = int(input(f"Ingrese el numero #{contador+1}: "))
    lista.append(pedir)

print(f"La lista resultante es: {lista}")
primos = [primo for primo in lista if primo % 2 != 0]
mayor = max(primos)
posicion = primos.index(mayor)

print(f"El numero par mayor esta en la posicion {posicion+1}")