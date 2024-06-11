# Filtrar elementos (Numeros Primos)
pregunta = int(input("Que quiere filtrar (0 = numeros , 1 = textos): "))

if pregunta == 0:
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("La lista de los numeros es: ", numeros )

    pares = [seleccion for seleccion in numeros if seleccion%2 == 0]

    print(pares)

elif pregunta == 1:
    textos = ["Adios", "Holanda", "Oso", "Leon", "Chino", "Dominicano"]
    print("La lista de textos es:", textos)

    letraA = [seleccion for seleccion in textos if "a" in seleccion or "A" in seleccion]

    print("El filtrado de la letra concluyo en: ", letraA)

else:
    quit("Seleccione bien")