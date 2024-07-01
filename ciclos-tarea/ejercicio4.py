# 4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.

numeroUno = int(input("Dame el primer numero: \n"))
numeroDos = int(input("Dame el segundo numero: \n"))

for enteros in range(numeroUno, numeroDos+1):
    print(enteros, end=", ")