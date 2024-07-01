# 10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.

numeroDado = int(input("Dame un numero: \n"))

suma = [enteros for enteros in range(1, numeroDado+1)]

print(sum(suma))
