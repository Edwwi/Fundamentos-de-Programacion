# Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído.
lista = []

def es_primo(primo):
    if primo <= 1:
        return False
    for i in range(2, int(primo ** 0.5) + 1):
        if primo % i == 0:
            return False
    return True

for contador in range(10):
    pedir = int(input(f"Ingrese el numero #{contador+1}: "))
    lista.append(pedir)

print(f"La lista resultante es: {lista}")
primos = [primo for primo in lista if es_primo(primo)]
mayor = max(primos)
posicion = primos.index(mayor)

print(f"El numero par mayor esta en la posicion {posicion+1}")