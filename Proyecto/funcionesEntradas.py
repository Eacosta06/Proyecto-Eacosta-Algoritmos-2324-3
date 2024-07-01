"""En este archivo se encuentran todas las funciones relacionadas
a la compra de tickets y el registro de clientes teniendo en cuenta
la cedula."""

from cliente import Cliente
from tickets import Entrada
from tickets import EntradaVIP
import funcionesEstadisticas as fE

def numerico(numero):
    """Verifica que un numero sea INT"""
    if numero.isnumeric():
        return int(numero)
    else:
        return False

def numero_vampiro(cedula):
    """Esta función debería verificar si una cedula
    es un numero vampiro"""
    return False


def crear_cliente(cedula):
    """Esta función crea el objeto de un cliente"""
    nombre = input("\nPor favor indique su nombre: \n -> ")
    while True:
        edad = input("\nPor favor indique su edad: \n -> ")
        if numerico(edad):
            edad = numerico(edad)
            cliente = Cliente(nombre, cedula, edad)
            return cliente
        else:
            print("\nSu edad debe ser un valor numérico. Intentelo de nuevo")


def buscar_cliente(clientes_lista, cedula):
    #Esta función verifica si un cliente ya existe. En caso contrario lo crea.
    cliente_S = None
    for cliente in clientes_lista:
        if cliente.ver_cedula() == cedula:
            cliente_S = cliente
            return cliente_S
    cliente_S = crear_cliente(cedula)
    clientes_lista.append(cliente_S)
    return cliente_S

def buscar_partido(partidos):
    #Esta función busca un partido por su numero asociado
    while True:
        print("\nPor favor indique el numero de partido que desea comprar:")
        numero = input("-> ")
        if numerico(numero):
            for partido in partidos:
                if partido.ver_numero() == int(numero):
                    return partido
            print("No se ha encontrado un partido relacionado a ese número. Intentelo de nuevo.")
        else:
            print("\nEl número de partido debe ser un valor numérico. Intentelo de nuevo.")

def verificar_asiento(partido, estadio, seleccion, tipo):
    #Esta función verifica si un asiento ya existe
    if tipo == "VIP":
        if estadio.existe_VIP(seleccion):
            if partido.verificar_VIP(seleccion):
                return True
            else:
                print("\nEl asiento seleccionado ya ha sido ocupado. Intentelo de nuevo.")
                return False
        else:
            print("\nEl asiento seleccionado no existe. Intentelo de nuevo.")
            return False
    else:
        if estadio.existe_General(seleccion):
            if partido.verificar_General(seleccion):
                return True
            else:
                print("\nEl asiento seleccionado ya ha sido ocupado. Intentelo de nuevo.")
                return False
        else:
            print("\nEl asiento seleccionado no existe. Intentelo de nuevo.")
            return False

def mostrar_asientos(partido, tipo):
    #Muestra los asientos de un estadio
    estadio = partido.estadios()
    if tipo == "VIP":
        estadio.ver_asientosVIP()
        while True:
            seleccion = input("\nIngrese el asiento de su preferencia: \n -> ")
            if numerico(seleccion):
                seleccion = numerico(seleccion)
                asiento = verificar_asiento(partido, estadio, seleccion, "VIP")
                if asiento:
                    return seleccion
    else:
        estadio.ver_asientosGen()
        while True:
            seleccion = input("\nIngrese el asiento de su preferencia: \n -> ")
            if numerico(seleccion):
                seleccion = numerico(seleccion)
                asiento = verificar_asiento(partido, estadio, seleccion, "General")
                if asiento:
                    return seleccion

def mostrar_precio(tipo, cliente):
    #Muestra la factura al cliente para proceder con el pago.
    if tipo == "VIP":
        if numero_vampiro(cliente.ver_cedula()):
            print("Debido a que su cédula es un número vampiro se le ha otorgado un 50%", end= " ")
            print("de descuento")
            precio = 75
            descuento = 0.5
        else:
            precio = 75
            descuento = 1
    else:
        if numero_vampiro(cliente.ver_cedula()):
            precio = 35
            descuento = 0.5
        else:
            precio = 35
            descuento = 1
    Iva = fE.IVA(precio*descuento)
    print("\n--------------------------------------")
    print("               CHECKOUT")
    print("--------------------------------------")
    print(f"Cédula: {cliente.ver_cedula()}")
    print(f"Nombre: {cliente.ver_nombre()}")
    print("\n \n \n \nEntrada " + tipo + f":                    {precio}")
    if descuento != 1:
        print(f"Descuento:                               {descuento*100}%")
    print(f"\n \n \n \nSubtotal:                           {precio*descuento}")
    print(f"IVA:                               {Iva}")
    print("--------------------------------------")
    print(f"Total:                            ${precio*descuento + Iva}")
    print("\n \n¿Desea continuar con el pago?: \n 1. Si \n 2. No")
    seleccion = input("-> ")
    while True:
        if seleccion == "1":
            print("\n Pago Procesado.")
            return True
        elif seleccion == "2":
            print("\n Cancelando compra...")
            return False
        else:
            print("El valor ingresado es incorrecto. Intentelo de nuevo.")


def crear_ticket(partido, cliente):
    #Crea un ticket y muestra su código respectivo
    numero = f"{partido.ver_numero()}"
    while True:
        print("\nPor favor inidique que tipo de asiento desea: \n 1. General - $35 \n 2. VIP - $75")
        seleccion = input("-> ")
        if seleccion == "1":
            asiento = mostrar_asientos(partido, "General")
            codigo = f"{numero}_{asiento}_Gen"
            if mostrar_precio("General", cliente):
                anadir_ticket(partido, cliente, Entrada(codigo), asiento, "General")
                print(f"\nEl código de su ticket es: {codigo}")
                break
            else:
                break
        elif seleccion == "2":
            asiento = mostrar_asientos(partido, "VIP")
            codigo = f"{numero}_{asiento}_VIP"
            if mostrar_precio("VIP", cliente):
                anadir_ticket(partido, cliente, EntradaVIP(codigo), asiento, "VIP")
                print(f"\nEl código de su ticket es: {codigo}")
                break
            else:
                break
        else:
            print("Se ha ingresado una opción inválida. Intentelo de nuevo.")


def anadir_ticket(partido, cliente, ticket, asiento, tipo):
    #añade un ticket a los tickets del cliente
    cliente.anadir_ticket(ticket)
    if tipo == "General":
        partido.añadir_General(asiento)
    else:
        partido.añadir_VIP(asiento)



def comprar_ticket(clientes_lista, partidos):
    #Menú principal del módulo compra de tickets.
    while True:
        print("\n---------------------------------")
        print("******Compra de Tickets******")
        print("---------------------------------\n")
        cedula = input("Por favor indique su número de cédula: \nEscriba \"exit\" para regresar \n-> ")
        if numerico(cedula):
            cedula = numerico(cedula)
            cliente = buscar_cliente(clientes_lista, cedula)
            partido = buscar_partido(partidos)
            crear_ticket(partido, cliente)
        elif cedula == "exit":
            break
        else:
            print("\nSe ha introducido un valor incorrecto. Intentelo de nuevo. \nRecuerde que la cédula debe ser un valor numérico")
