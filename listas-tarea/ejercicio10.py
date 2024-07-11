#10 Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.
lista = []


for contador in range(10):
    pedir = int(input(f"Ingrese el número #{contador + 1}: "))
    lista.append(pedir)

print(f"La lista resultante es: {lista}")


numeroAdicional = int(input("Ingrese un número adicional: "))


divisores = 0
for numero in lista:
    if numeroAdicional % numero == 0:
        divisores += 1

print(f"El número {numeroAdicional} tiene {divisores} divisores exactos entre los valores almacenados en la lista.")
