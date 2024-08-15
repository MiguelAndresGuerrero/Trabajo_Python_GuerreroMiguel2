import json
from datetime import datetime

# Función para abrir archivo JSON
def abrir_archivo(nombre_archivo="Info.json"):
    try:
        with open(nombre_archivo, "r") as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        return {}

# Función para guardar en archivo JSON
def guardar_archivo(nombre_archivo="Info.json", data=None):
    with open(nombre_archivo, "w") as outfile:
        json.dump(data, outfile, indent=4)

# Función para registrar venta
def registrar_venta(data):
    cliente = input("Ingrese el nombre del cliente: ")

    # Validar si el cliente ya tiene un pedido activo
    pedidos = [pedido for pedido in data if pedido['seccion'] == 'Pedidos']
    pedidos_cliente = [p for p in pedidos if p['cliente'] == cliente and p['estado'] != 'Creado']
    
    if pedidos_cliente:
        print(f"El cliente {cliente} ya tiene un pedido activo")
        return
    
    fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Mostrar menú de secciones
    seccion_elegida = elegir_seccion(data)
    if not seccion_elegida:
        print("Sección no válida")
        return

    # Mostrar productos de la sección elegida
    productos_disponibles = seccion_elegida.get("productos", [])
    
    if not productos_disponibles:
        print("No hay productos disponibles en esta sección")
        return

    print("Productos disponibles:")
    for i, producto in enumerate(productos_disponibles):
        print(f"{i + 1}. {producto['nombre']} - Precio: {producto['precio']}")
    
    producto_id = int(input("Seleccione el ID del producto: ")) - 1
    if producto_id < 0 or producto_id >= len(productos_disponibles):
        print("Producto no válido")
        return

    producto = productos_disponibles[producto_id]
    cantidad = int(input("Ingrese la cantidad: "))

    # Registrar la venta
    nuevo_pedido = {
        "id": len(pedidos) + 1,
        "seccion": "Pedidos",
        "cliente": cliente,
        "productos": [
            {
                "categoria": producto["categoria"],
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": cantidad
            }
        ],
        "estado": "Creado"
    }

    data.append(nuevo_pedido)
    guardar_archivo("Info.json", data)
    print(f"Venta registrada con éxito para {cliente} el {fecha_venta}")

# Función para elegir una sección
def elegir_seccion(data):
    print("==============================")
    print("      MENU DE SECCIONES       ")
    print("==============================")
    secciones = [seccion for seccion in data if 'productos' in seccion]

    for i, seccion in enumerate(secciones):
        print(f"{i + 1}. {seccion['seccion']}")

    try:
        seccion_id = int(input("Seleccione la sección: ")) - 1
        if 0 <= seccion_id < len(secciones):
            return secciones[seccion_id]
        else:
            print("Sección no válida")
    except ValueError:
        print("Debe ingresar un número válido")
    return None

# Mostrar pedidos de un cliente
def mostrar_pedido(data, cliente):
    pedidos_cliente = [pedido for pedido in data if pedido['seccion'] == 'Pedidos' and pedido['cliente'] == cliente]
    
    if not pedidos_cliente:
        print(f"No hay pedidos registrados para {cliente}")
        return

    for pedido in pedidos_cliente:
        print(f"Cliente: {cliente} | Estado: {pedido['estado']}")
        for producto in pedido['productos']:
            print(f"  - Producto: {producto['nombre']} | Precio: {producto['precio']} | Categoria: {producto['categoria']}")

# Menú de cliente
def menu_cliente(data):
    while True:
        print("==============================")
        print("         Menú Cliente         ")
        print("==============================")
        print("1. Ver productos por sección  ")
        print("2. Comprar Producto           ")
        print("3. Ver mis pedidos            ")
        print("4. Salir                      ")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_productos_por_seccion(data)

        elif opcion == "2":
            registrar_venta(data)

        elif opcion == "3":
            cliente = input("Ingrese su nombre para ver sus pedidos: ")
            mostrar_pedido(data, cliente)

        elif opcion == "4":
            break

        else:
            print("Opción inválida.")

# Mostrar productos por sección
def mostrar_productos_por_seccion(data):
    seccion = elegir_seccion(data)

    if seccion:
        print(f"===== Productos de {seccion['seccion']} =====")

        for  producto in seccion["productos"]:
            print(f"{producto['nombre']} - Precio: {producto['precio']}")
    
    else:
        print("Sección no válida")

# Menú principal
def menu_principal():
    data = abrir_archivo("Info.json")

    while True:
        print("==============================")
        print("        MENÚ PRINCIPAL        ")
        print("==============================")
        print("1. Cliente                    ")
        print("2. Salir                      ")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_cliente(data)

        elif opcion == "2":
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()

#Creado por Miguel Guerrero C.C 1090381839