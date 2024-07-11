#9 Leer 10 números enteros, almacenarlos en una lista y calcular la factorial a cada uno de los números leídos almacenándolos en otra lista
import math

lista = []

for contador in range(10):
    pedir = int(input(f"Ingrese el número #{contador + 1}: "))
    lista.append(pedir)

print(f"La lista resultante es: {lista}")


listaFactoriales = []

for numero in lista:
    factorial = math.factorial(numero)  
    listaFactoriales.append(factorial)

print(f"La lista de factoriales es: {listaFactoriales}")
