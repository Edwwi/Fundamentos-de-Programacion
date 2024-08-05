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
    print("Despues sigo")

def listadoProductos():
    print("Despues sigo")

def agregarProductos():
    print("Despues sigo")

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
        