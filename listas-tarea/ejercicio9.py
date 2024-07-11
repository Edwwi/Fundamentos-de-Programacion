import math

lista = []

# Leer 10 números enteros
for contador in range(10):
    pedir = int(input(f"Ingrese el número #{contador + 1}: "))
    lista.append(pedir)

print(f"La lista resultante es: {lista}")

# Lista para almacenar los factoriales
listaFactoriales = []

for numero in lista:
    factorial = math.factorial(numero)  # Usar math.factorial para calcular el factorial
    listaFactoriales.append(factorial)

print(f"La lista de factoriales es: {listaFactoriales}")
