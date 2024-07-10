#5 Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_digitos_pares(numero):
    contador_pares = 0
    for digito in str(numero):
        if int(digito) % 2 == 0:
            contador_pares += 1
    return contador_pares

lista = []

for contador in range(10):
    pedir = int(input(f"Ingrese el número #{contador+1}: "))
    lista.append(pedir)

print(f"La lista resultante es: {lista}")

primos = [numero for numero in lista if es_primo(numero)]

if primos:
    max_pares = -1
    primo_con_max_pares = None
    for primo in primos:
        pares = contar_digitos_pares(primo)
        if pares > max_pares:
            max_pares = pares
            primo_con_max_pares = primo

    posicion = lista.index(primo_con_max_pares)
    print(f"El número primo con mayor cantidad de dígitos pares es {primo_con_max_pares} y está en la posición {posicion + 1}.")
