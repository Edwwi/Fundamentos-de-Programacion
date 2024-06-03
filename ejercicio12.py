print("Juego\nMe daras dos numeros de esos sacare su diferencia si:\n » Su resultado es un numero par te mostrare la suma entre los 2 numeros \n » Si su resultado es un numero primo te mostrare su producto \n » Si termina en cuatro el resultado te mostrare los digitos de los numeros\n")

primerNumero = int(input("Ingrese el primer numero: "))
segundoNumero = int(input("Ingrese el segundo numero: "))

numerosPrimos = [2, 3, 5, 7] # Numeros primos

resultado = abs(primerNumero - segundoNumero)


if resultado %2 == 0: #Identificar si un numero es par o no con el modulo 2
    while resultado != 0:
        print("El numero es un numero par: \n» La suma de los numeros es: ", primerNumero%10 + segundoNumero%10)
        break
elif resultado in numerosPrimos: # Verificar que esta en la lista de los numeros primos
    print("Este numero es un numero primo menor a 10 \n» La multiplicacion de los numeros es: ", primerNumero*segundoNumero)
elif resultado%10 == 4: # Si el resultado termina en 4 muestra los digitos por seperado
    while resultado != 0:
        print("La diferencia de los numeros", primerNumero, "y ", segundoNumero, " terminan en 4\nte mostrare los digitos por separado de cada numero:")
        
        print("Digitos del primero numero ({primerNumero}): ")
        for digitos in str(primerNumero):
            print(digitos)
        print("Digitos del primero numero ({segundoNumero}): ")
        for digitos in str(segundoNumero):
            print(digitos)
else:
    print("El resultado no cumple con ninguno de los requisitos")