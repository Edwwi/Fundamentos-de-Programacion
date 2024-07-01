# 2. Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.

numeroDado = int(input("Dame un numero: \n"))

pares = [anteriores for anteriores in range(1, numeroDado+1)if anteriores%2 == 0]
print("Los numeros pares del numero ", numeroDado, "son: \n", pares)
    
    