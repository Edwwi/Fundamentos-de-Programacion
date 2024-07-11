#7 Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista
lista = []

for contador in range(10):
    pedir = int(input(f"Ingrese el número #{contador + 1}: "))
    lista.append(pedir)

print(f"La lista resultante es: {lista}")

promedio = sum(lista) // len(lista)  

print(f"El promedio entero de los datos de la lista es: {promedio}")