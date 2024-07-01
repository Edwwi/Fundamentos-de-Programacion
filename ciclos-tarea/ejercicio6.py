# 6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.

numeroUno = int(input("Dame el primer numero: \n"))
numeroDos = int(input("Dame el segundo numero: \n"))

for anteriores in range(numeroUno, numeroDos+1):
    print(anteriores, end=",")
for separados in str(anteriores):
    print(separados)