import json
from datetime import datetime

#Nomabre del usuario
Name=input("Bienvenido, ingresa tu nombre: ")

# Login de usuarios
print("¿Cómo quieres ingresar?")
print("""
      =======================================
                    MENU PRINCIPAL
      =======================================
        1. Cliente
        2. Vendedor
        3. salir
    """)
rango = int(input("¿Cuál es tu forma de acceso? "))

# Conexión al archivo JSON general
def abrir_archivo():
    with open("Info.json", "r") as openfile:
        return json.load(openfile)

def guardar_archivo(data):
    with open("Info.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

# Guardar las ventas y compras en un archivo JSON separado
def guardar_transacciones(transacciones):
    with open("Transacciones.json", "w") as outfile:
        json.dump(transacciones, outfile, indent=4)

def cargar_transacciones():
    try:
        with open("Transacciones.json", "r") as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        return []

# Inicializar el archivo de transacciones
transacciones = cargar_transacciones()

# Registro de ventas
def registrar_venta(data):
    fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Seleccionar paciente
    pacientes = data[3]["productos"]

    for i, entradas in enumerate(pacientes):
        print(f"{i+1}. {entradas['productos']}")
    paciente_id = int(input("Seleccione el ID del paciente: ")) - 1
    entradas = pacientes[paciente_id]
    
    # Seleccionar medicamento
    medicamentos = data[0]["productos"]

    for i, medicamento in enumerate(medicamentos):
        print(f"{i+1}. {medicamento['producto']} - Precio: {medicamento['precio']}")
    medicamento_id = int(input("Seleccione el ID del medicamento: ")) - 1
    medicamento = medicamentos[medicamento_id]
    
    # Registrar la venta
    venta = {
        "fecha": fecha_venta,
        "medicamento": {
            "nombre": ["producto"],
            "categoria": ["categotia"],
            "precio": ["precio"]
        }
    }
    transacciones.append(venta)
    guardar_archivo(data)
    guardar_transacciones(transacciones)
    print(f"Venta registrada con éxito el {fecha_venta}")

# Registro de compras
def registrar_compra(data):
    fecha_compra = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Seleccionar Entradas
    entradas= data[3]["productos"]

    for i, entradas in enumerate(entradas):
        print(f"{i+1}. {entrada['Nombre']}")
    entrada = int(input("Seleccione la entrada: ")) - 1
    entradas = entradas[entrada]
    
    # Seleccionar medicamento
    medicamentos = data[0]["productos"]

    for i, medicamento in enumerate(medicamentos):
        print("-------------------------------------------------------------------------------------------------------------")
        print(f"{i+1}. {medicamento['producto']} - Precio de compra: {medicamento['precio']}")
        print("-------------------------------------------------------------------------------------------------------------")
    medicamento_id = int(input("Seleccione el ID del medicamento: ")) - 1
    medicamento = medicamentos[medicamento_id]
    
    # Registrar la cantidad comprada
    cantidad = int(input("Ingrese la cantidad comprada: "))
    
    # Actualizar el stock
    medicamento["stock"] = str(int(medicamento["stock"]) + cantidad)
    
    # Registrar la compra
    compra = {
        "fecha": fecha_compra,
        "medicamento": {
            "nombre": medicamento["producto"],
            "cantidad": cantidad,
            "precio_compra": medicamento["precio"]
        }
    }
    transacciones.append(compra)
    guardar_archivo(data)
    guardar_transacciones(transacciones)
    print(f"Compra registrada con éxito el {fecha_compra}")

# Menú de productos
def mostrar_productos(data):
    print("===========================")
    print("          Menu:            ")
    print("===========================")

    for productos in data[0]["productos"]:
        print(f"{productos['categoria']}: {productos['nombre']} - Precio: {productos['precio']}")

# Menú de cliente
def menu_cliente(data):

    while True:
        print("============================")
        print("            MENU            ")
        print("============================")
        print("1. Ver el Menu ")
        print("2. Comprar producto ")
        print("3. Salir ")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_productos(data)
                
        elif opcion == "2":
            registrar_venta(data)
                
        elif opcion == "3":
            print("Gracias por usar el programa")
            break

        else:
            print("Opción inválida")

# Menú de moderador
def menu_moderador(data):

    while True:
        print("=============================")
        print("    BIENVENIDO VENDEDOR      ")
        print("=============================")
        print("1. Revisar productos")
        print("2. Revisar compras")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_productos(data)
                
        elif opcion == "2":
            registrar_compra(data)
                
        elif opcion == "3":
            print("Gracias por usar el programa, Hasta la proxima :D")
            break
        
        else:
            print("Opción inválida, Selecciona una valida")

# Cargar datos
data = abrir_archivo()

if rango == 1:
    menu_cliente(data)
elif rango:
    print("opcion no valida")

#Creado por Miguel Guerrero C.C 1090381839