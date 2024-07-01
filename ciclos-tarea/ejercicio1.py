# 1. Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído.

numeroDado = int(input("Dame un numero: \n"))

for anteriores in range(1, numeroDado+1):
    print(anteriores, end=", ")