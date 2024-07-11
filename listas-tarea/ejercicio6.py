#6 Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos
lista = []

for contador in range(10):
    pedir = int(input(f"Ingrese el número #{contador + 1}: "))
    lista.append(pedir)

print(f"La lista resultante es: {lista}")

posiciones = []
for indice, numero in enumerate(lista):
    if len(str(abs(numero))) > 3: 
        posiciones.append(indice + 1)

if posiciones:
    print(f"Los números con más de 3 dígitos están en las posiciones: {posiciones}")
else:
    print("No se encontraron números con más de 3 dígitos en la lista.")
