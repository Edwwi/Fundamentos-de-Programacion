# 9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.

primerNumero = 25
segundoNumero = 205

for enteros in range(primerNumero, segundoNumero+1):
    if enteros%10 ==6:
        print(enteros, end=", ")