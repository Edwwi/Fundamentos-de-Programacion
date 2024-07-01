# 3. Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído.

numeroDado = int(input("Dame un numero: \n"))

divisores = [divisor for divisor in range(1, numeroDado+1) if numeroDado%divisor == 0]
print("Los divisores del numero ", numeroDado, "son: \n", divisores)