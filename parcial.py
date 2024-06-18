sistema = "S"

while sistema == "S": 
  estudiantes = {"Nombre" : "", "Matricula" : ""}
  
  estudiantes["Nombre"] = input("Ingrese el nombre del estudiante: ")
  estudiantes["Matricula"] = input("Ingrese su matricula: ")
  print(estudiantes)
  
  primeraNota = int(input("Ingrese la primera nota: "))
  segundaNota = int(input("Ingrese la segunda nota: "))
  terceraNota = int(input("Ingrese la tercera nota: "))
  cuartaNota = int(input("Ingrese la cuarta nota: "))

  notas = []
  notas.append(primeraNota)
  notas.append(segundaNota)
  notas.append(terceraNota)
  notas.append(cuartaNota)
  if notas[0] < 0 or notas[1] > 100 or notas[1] < 0 or notas[1] > 100 or notas[2] < 0 or notas[2] > 100 or notas[3] < 0 or notas[3] > 100:
    print("Las notas deben ser mayores o iguales a 0 y menores o iguales a 100")
    break
  else:
    promedio = sum(notas)/len(notas )
  


    print("El promedio de ", estudiantes["Nombre"], " es de ", promedio)
  sistema = input("Desea hacer lo mismo con otro estudiante? (S/N): ")