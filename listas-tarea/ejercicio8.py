#8 Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay.
lista = []

for contador in range(10):
    pedir = int(input(f"Ingrese el número #{contador + 1}: "))
    lista.append(pedir)

print(f"La lista resultante es: {lista}")

contadorNegativos = 0
for numero in lista:
    if numero < 0:
        contadorNegativos += 1

print(f"La cantidad de números negativos en la lista es: {contadorNegativos}")