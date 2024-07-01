"""En este documento van todas las funciones destinadas
a estadisticas y algunos calculos"""

import funcionesRestaurant as fR
import funcionesObjetos as fO

def IVA(precio):
    #Retorna el IVA del precio otorgado.
    final = float(precio)*0.16
    return round(final, 2)

def tabla_productos(productos):
    print("\n Producto        Vendidos")
    for i, producto in enumerate(productos):
        if i < 3:
            print(f"{producto["nombre"]}  {producto["vendidos"]}")
        else:
            break


def organizar_productos(productos):
    #Organiza la lista de productos
    print("Organizando Productos")
    Lorganizada = []
    for producto in productos:
        if len(Lorganizada) == 0:
            Lorganizada.append(producto)
        else:
            for i, pro in enumerate(Lorganizada):
                if producto["vendidos"] > pro["vendidos"]:
                    Lorganizada.insert(i, producto)
    tabla_productos(Lorganizada)

def productos_vendidos(productos):
    print("analizando productos")
    Lproductos = []
    for producto in productos:
        Dproducto = {}
        Dproducto["nombre"] = producto.ver_nombre()
        Dproducto["vendidos"] = producto.ver_cantidad()
        Lproductos.append(Dproducto)
    organizar_productos(Lproductos)

def decifrar_numero(codigo):
    lista = codigo.split("_")
    return int(lista[0])

def asistencia_tickets(clientes, partido):
    asistencia = 0
    tickets = 0
    for cliente in clientes:
        for ticket in cliente.mostrar_tickets():
            num = decifrar_numero(ticket.ver_codigo())
            if num == partido.ver_numero():
                tickets += 1
                if ticket.ver_asistencia():
                    asistencia += 1
    return tickets, asistencia

def mostrar_tabla(partidos):
    print("Equipo Local    Equipo Visitante    Estadio           Entradas     Asistencia   Relacion ")
    for partido in partidos:
        for key in partido:
            print(partido[key], end= "  ")
        print("\n")
    Masistencia = partidos[0]
    print(f"\nEl partido con mayor asistencia fue {Masistencia["Equipo Local"]} VS {Masistencia["Equipo Visitante"]}")
    

def organizar_asistencia(partidos):
    """Organiza la lista de asistencia."""
    Lorganizada = []
    print("Organizando partidos... Esto puede tardar un momento.")
    for partido in partidos:
        if len(Lorganizada) == 0:
            Lorganizada.append(partido)
        else:
            for i, prt in enumerate(Lorganizada):
                if partido["asistencia"] > prt["asistencia"]:
                    Lorganizada.insert(i, partido)
    mostrar_tabla(Lorganizada)

def asistencia_partidos(partidos, equipos, clientes, estadios):
    Lpartidos = []
    for partido in partidos:
        Dpartido = {}
        EquipoL, EquipoV = partido.ver_equipos()
        Dpartido["Equipo Local"] = fO.buscar_equipos(equipos, EquipoL)
        Dpartido["Equipo Visitante"] = fO.buscar_equipos(equipos, EquipoV)
        Dpartido["Estadio"] = fO.buscar_estadios(estadios, partido.estadios())
        tickets, asistencia = asistencia_tickets(clientes, partido)
        Dpartido["Tickets"] = tickets
        Dpartido["asistencia"] = asistencia
        if asistencia != 0:
            Dpartido["relacion"] = round((asistencia/tickets)*100, 2)
        else:
            Dpartido["relacion"] = None
        Lpartidos.append(Dpartido)
    organizar_asistencia(Lpartidos)
        


def suma_gastos(cliente, productos):
    suma = 0
    if len(cliente.ver_productos()) != 0:
        for productoC in cliente.ver_productos():
            for producto in productos:
                if producto.ver_nombre() == productoC:
                    suma += producto.ver_precio()
        return suma
    else:
        return 0

def promedio_VIP(lista_gastos):
    gastosTotales = 0
    longitud = len(lista_gastos)
    for gasto in lista_gastos:
        gastosTotales += gasto
    if longitud != 0:
        promedio = (gastosTotales / longitud)
        print(f"El promedio de gastos VIP es de: ${promedio}")
    else:
        print(f"El promedio de gastos VIP es de: $0")

def gastos_VIP(clientes, productos):
    gastos_clientes = []
    for cliente in clientes:
        for ticket in cliente.mostrar_tickets():
            if ticket.ver_vip():
                gastosP = suma_gastos(cliente, productos)
                gastos = gastosP + 75
                gastos_clientes.append(gastos)
    promedio_VIP(gastos_clientes)
    

def estadisticas(clientes, estadios, equipos, partidos):
    #Menú principal de la gestión estadística.
    productos = fR.lista_productos(estadios)
    while True:
        print("\n******Indicadores de Gestión******")
        print("\n¿Que estadísticas deseas ver?:")
        print(" 1. Promdeio de Gastos VIP\n 2. Asistencia de Partidos\n 3. Productos más vendidos\n 4. Clientes con más boletos\n 5. Salir")
        seleccion = input("-> ")
        if seleccion == "1":
            gastos_VIP(clientes, productos)
        elif seleccion == "2":
            asistencia_partidos(partidos, equipos, clientes, estadios)
        elif seleccion == "3":
            productos_vendidos(productos)
        elif seleccion == "4":
            pass
        elif seleccion == "5":
            break
        else:
            print("Se ha introducido una opción inválida. Intentelo de nuevo.")