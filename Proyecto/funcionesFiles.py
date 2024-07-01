
import requests
import funcionesObjetos as fO
import pickle as pk


def import_API():
    #Importa los archivos desde la API y crea los objetos respectivos.
    print("\nImportando desde la API... \n")
    Requipos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")
    Rpartidos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")
    Restadios = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")

    Dequipos = Requipos.json()
    Dpartidos = Rpartidos.json()
    Destadios = Restadios.json()
    clientes = []

    print("Creando Objetos... \n")

    estadios, equipos, partidos = fO.crear_objetos(Dequipos, Destadios, Dpartidos)

    return estadios, equipos, partidos, clientes

def abrir_archivos():
    #Intenta abrir los archivos. En caso contrario los descarga de la API
    try:
        print("\nBuscando archivos...\n")
        with open("estadios.txt", "rb") as e:
            estadios = pk.load(e)
        with open("partidos.txt", "rb") as p:
            partidos = pk.load(p)
        with open("clientes.txt", "rb") as c:
            clientes = pk.load(c)
        with open("equipos.txt", "rb") as eq:
            equipos = pk.load(eq)
        print("Cargando Archivos...")
        return estadios, equipos, partidos, clientes
    except FileNotFoundError:
        return import_API()

def guardar_archivos(estadios, equipos, partidos, clientes):
    #Guarda los datos en sus archivos respectivos. Si no existen los crea.
    with open("estadios.txt", "wb") as e:
        pk.dump(estadios, e)
    with open("partidos.txt", "wb") as p:
        pk.dump(partidos, p)
    with open("clientes.txt", "wb") as c:
        pk.dump(clientes, c)
    with open("equipos.txt", "wb") as eq:
        pk.dump(equipos, eq)