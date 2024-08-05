productos = {"001:" : {"nombre": "Producto 1", "precio" : "$200"}, "002" : {"nombre": "Producto 1", "precio" : "$200"}}

facturas = []

def opciones(): # Menu Principal
    print("[1] Crear Factura")
    print("[2] Ver Facturas")
    print("[3] Productos")
    print("[4] Añadir Productos")
    print("[5] Salir")


# Opciones anteriores:
def crearFactura():
    print("Despues sigo")

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
        