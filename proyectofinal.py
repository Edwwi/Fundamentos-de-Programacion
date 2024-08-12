productos = {"001" : {"nombre": "Cereal", "precio" : 500}, "002" : {"nombre": "Carne", "precio" : 200}}

facturas = []

def opciones(): # Menu Principal
    print("[1] Crear Factura")
    print("[2] Ver Facturas")
    print("[3] Productos")
    print("[4] Añadir Productos")
    print("[5] Salir")


# Opciones anteriores:
def crearFactura():
    factura = {}
    factura["productos"] = []
    total = 0
    
    print("Seleccione los productos para la factura (ingrese 'N' para finalizar): ")

    while True:
        codigo = input("» Ingrese el codigo del producto: ")
        if codigo == "N":
            break
        elif codigo in productos:
            cantidad = int(input(f"» Ingrese la cantidad de '{productos[codigo]['nombre']}': "))
            print(f"Tienes {cantidad} de {productos[codigo]['nombre']}")
            subtotal = productos[codigo]['precio']*cantidad
            total += subtotal
            factura["productos"].append({
    "codigo": codigo,
    "nombre": productos[codigo]["nombre"],
    "precio": productos[codigo]["precio"],
    "cantidad": cantidad,
    "subtotal": subtotal
})
            print(f"{cantidad} x {productos[codigo]['nombre']} agregado a la factura. Subtotal: {subtotal}")
        else:
            print("Codigo de producto invalido")

        factura["total"] = total
        factura["numero"] = len(facturas) + 1
        facturas.append(factura)
        print(f"Factura creada exitosamente. Total: {total}")



 
def verFacturas():

    if not facturas:
        print("No hay facturas. crea una")
        return
    
    for factura in facturas:
        print(f"Factura #{factura['numero']}:")
        for producto in factura["productos"]:
            print(f" - {producto['cantidad']} x {producto['nombre']} (Código: {producto['codigo']}) - Subtotal: {producto['subtotal']}")
        print(f"Total: ${factura['total']}")
        

def listadoProductos():
    print("Lista de productos:")
    for codigo, detalles in productos.items():
        print(f"{codigo}: {detalles['nombre']} - Precio: {detalles['precio']}")

def agregarProductos():
    codigo = input("» Ingrese el código del nuevo producto: ")
    if codigo in productos:
        print("El código ya existe.")
        return
    
    nombre = input("» Ingrese el nombre del producto: ")
    precio = float(input("» Ingrese el precio del producto: "))
    
    productos[codigo] = {"nombre": nombre, "precio": precio}
    print(f"Producto '{nombre}' añadido exitosamente.")

    
# Bucle Principal

while True:
    opciones()
    opcion = input("» Seleccione una opcion: ")
    opcion = int(opcion)

    if opcion == 1:
        crearFactura()
    elif opcion == 2:
        verFacturas()
    elif opcion == 3:
        listadoProductos()
    elif opcion == 4:
        agregarProductos()
    else:
        print("Syntax error")
        break
        