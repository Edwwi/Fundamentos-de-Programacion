def tipoNumero(numero):
    if numero%2 == 0:
        print("Es par")
    elif numero%2 != 0:
        print("Es impar")
    

tipoNumero(int(input("Ingrese el numero para saber si es par o impar: ")))
