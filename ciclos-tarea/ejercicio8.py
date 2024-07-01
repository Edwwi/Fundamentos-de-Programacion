# 8. Mostrar en pantalla todos los pares comprendidos entre 20 y 200.

primerNumero = 20
segundoNumero = 200

for pares in range(primerNumero, segundoNumero+1):
    if pares % 2 ==0:
        print(pares, end=", ")