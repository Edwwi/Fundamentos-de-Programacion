notas = [90, 75, 89, 61, 83]

print("Las notas son: ", notas)
sumatoria = sum(notas)
print("La sumatoria de las notas es en total: ", sumatoria)

notasEnTuplas = (90, 75, 89, 61, 83)
producto = int(input("Por cuanto quieres incrementar las notas?: "))
for separado in notasEnTuplas:
    print(producto*separado)

media = sum(notas) / len(notas) # Sum = Sumatoria de todas las notas y Len = cuenta la cantidad de elemntos de la lista
print("La media de notas es: ", media)