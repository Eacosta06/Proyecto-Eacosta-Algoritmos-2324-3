"""En este archivo se encuentran las funciones que crean cada uno de los objetos."""

from estadios import Estadio
from restaurants import Restaurante
from productos import Bebida
from productos import Comida
from productos import BebidaAchl
from equipos import Equipo
from partidos import Partido

def crear_productos(productos_lista):
    #Esta función crea cada instancia de la clase producto desde la API
    productos = []
    for producto in productos_lista:
        for key in producto:
            if key == "name":
                nombre = producto[key]
            elif key == "quantity":
                cantidad = producto[key]
            elif key == "price":
                precio = producto[key]
            elif key == "adicional":
                adicional = producto[key]
            elif key == "stock":
                stock = producto[key]
        if adicional == "alcoholic":
            productos.append(BebidaAchl(nombre, cantidad, precio, stock))
        elif adicional == "non-alcoholic":
            productos.append(Bebida(nombre, cantidad, precio, stock))
        else:
            productos.append(Comida(nombre, cantidad, precio, stock, adicional))
    return productos



def crear_restaurantes(restaurantes_lista):
    #Esta función crea cada instancia de la clase restaurante desde la API
    restaurantes = []
    for restaurante in restaurantes_lista:
        for key in restaurante:
            if key == "name":
                nombre = restaurante[key]
            elif key == "products":
                productos = crear_productos(restaurante[key])
        restaurantes.append(Restaurante(nombre, productos))
    return restaurantes

def crear_mapa(numero_asientos):
    """Esta función crea una matriz con filas de máximo 10 puestos,
    siendo la capacidad del estadio el n máximo"""
    mapa = []
    fila = []
    n = 1
    nFila = 1
    while n <= numero_asientos:
        if nFila < 10:
            fila.append(n)
            n += 1
            nFila += 1
        elif nFila == 10:
            fila.append(n)
            mapa.append(fila)
            fila = []
            nFila = 1
            n += 1
    if len(fila) != 0:
        mapa.append(fila)
    return mapa



def crear_estadios(estadio_lista):
    #Esta funcion crea el objeto de cada estadio desde la API
    estadios = []
    for estadio in estadio_lista:
        for key in estadio:
            if key == "restaurants":
                restaurantes = crear_restaurantes(estadio[key])
            elif key == "id":
                id = estadio[key]
            elif key == "name":
                nombre = estadio[key]
            elif key == "city":
                ubicacion = estadio[key]
            elif key == "capacity":
                for index, capacity in enumerate(estadio[key]):
                    if index == 0:
                        capacidadG = crear_mapa(capacity)
                    elif index == 1:
                        capacidadVIP = crear_mapa(capacity)
                    
        estadios.append(Estadio(nombre, id, ubicacion, capacidadG, capacidadVIP, restaurantes))
    return estadios
        
def crear_equipos(equipos_lista):
    #Esta función crea cada instancia de la clase equipo desde la API
    equipos = []
    for equipo in equipos_lista:
        for key in equipo:
            if key == "id":
                id = equipo[key]
            elif key == "code":
                codigo = equipo[key]
            elif key == "name":
                nombre = equipo[key]
            elif key == "group":
                grupo = equipo[key]
        equipos.append(Equipo(nombre, id, codigo, grupo))
    return equipos

def buscar_equipos(equipos_lista, codigo):
    #Busca un equipo por su ID
    for equipo in equipos_lista:
        if equipo.equipo_id() == codigo:
            return equipo

def buscar_estadios(estadios_lista, id):
    #Esta función busca el estadio cuyo id es el proporcionado.
    for estadio in estadios_lista:
        if estadio.buscar_id() == id:
            return estadio

def crear_partido(partidos_lista, equipos, estadios):
    #Esta función crea cada instancia de la clase partido desde la API
    partidos = []
    for partido in partidos_lista:
        for key in partido:
            if key == "id":
                id = partido[key]
            elif key == "number":
                numero = partido[key]
            elif key == "date":
                fecha = partido[key]
            elif key == "group":
                grupo = partido[key]
            elif key == "home":
                equipo = partido[key]
                equipoID = equipo["id"]
                eqL = buscar_equipos(equipos, equipoID)
            elif key == "away":
                equipo = partido[key]
                equipoID = equipo["id"]
                eqV = buscar_equipos(equipos, equipoID)
            elif key == "stadium_id":
                estadio = partido[key]
                estadioP = buscar_estadios(estadios, estadio)
        partidos.append(Partido(id, numero, eqL, eqV, fecha, estadioP, grupo))
    return partidos

def crear_objetos(Dequipos, Destadios, Dpartidos):
    #Llama otras funciones para retornar la lista de objetos creados.
    estadios = crear_estadios(Destadios)
    equipos = crear_equipos(Dequipos)
    partidos = crear_partido(Dpartidos, equipos, estadios)
    return estadios, equipos, partidos