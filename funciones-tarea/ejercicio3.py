def areaRectangulo(largo, ancho):
    area = largo * ancho
    return area

largo = int(input("Dame el largo de tu rectangulo: "))
ancho = int(input("Dame el ancho de tu rectangulo: "))

llamada = areaRectangulo(largo, ancho)
print(f"El area de tu rectangulo ({largo} x {ancho}) es: {llamada}")