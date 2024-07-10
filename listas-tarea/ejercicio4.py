# Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo

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

contador2 = 0
primos = []
digitos_primos = [2, 3, 5, 7]

for primo in lista:
    primerDigito = int(str(primo)[0])  # Obtener el primer dígito del número
    if es_primo(primo) and primerDigito in digitos_primos:
        primos.append(primo)
        contador2 += 1

print(f"La cantidad de números primos que empiezan por un dígito primo son: {contador2}")
print(f"Los números primos que cumplen con la condición son: {primos}")