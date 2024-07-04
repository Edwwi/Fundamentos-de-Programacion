dato="oso,perro,10,5 son animales"

animales = []
animales.append(dato.split(",")[0])
animales.append(dato.split(",")[1])

for animal in animales:
    if animal==animal[::-1]:
        print(f"{animal} es un palindromo.")
    else:
        print(f"{animal} no es un palindromo")

print(f"Tenemos {dato.split(",")[3][:1]} {animales[0]}")
print(f"Tenemos {dato.split(",")[2]} {animales[1]}")
print(f"Tanto {animales[0]} y {animales[1]} {dato.split(",")[3][1:14]}")