#5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.


numeroUno = int(input("Dame el primer numero: \n"))
numeroDos = int(input("Dame el segundo numero: \n"))

for numeros in range(numeroUno, numeroDos+1):
    if numeros % 10 == 4:
        print("Los numeros que terminan en cuatro del ", numeroUno, " al ", numeroDos, " son \n", numeros)