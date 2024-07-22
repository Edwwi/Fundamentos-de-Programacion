def conversionF(grados):
    formula = (grados*9/5) + 32
    return formula

llamado = conversionF(int(input("Cuantos grados celcius tienes?: ")))
print(f"Tienes {llamado} F")