print("Imprimo el nombre si tiene 3 o mas vocales")
nombre = input("Ingrese su nombre: ")
vocales = ["a", "e", "i", "o", "u"]
contadorVocales = 0

while True:
  for caracteres in nombre:
    if caracteres in vocales:
      contadorVocales += 1


  if contadorVocales == 3:
    print("El nombre ", nombre, " tiene 3 vocales, cumple con las condiciones")
    break
  elif contadorVocales > 3:
    print("El nombre ", nombre, " tiene ", contadorVocales, " vocales")
    break
  else:
    print("El nombre ", nombre, "no cumple con las condiciones, tiene ", contadorVocales, " intentalo denuevo!")
    nombre = input("Ingrese su nombre: ")
    contadorVocales = 0
    