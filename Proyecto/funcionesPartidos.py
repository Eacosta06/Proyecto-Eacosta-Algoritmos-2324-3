"""En este archivo se encuentran todas las funciones relacionadas a la gestión
y busqueda de partidos."""

def partido_pais(lista_partidos):
    #Busca partidos por pais
    country = input("\nPor favor indique el país: \n -> ")
    partidos_pais = []
    for partido in lista_partidos:
        eqL, eqV = partido.ver_equipos()
        if eqL.ver_nombre() == country or eqL.equipo_code() == country:
            partidos_pais.append(partido)
        elif eqV.ver_nombre() == country or eqV.equipo_code() == country:
            partidos_pais.append(partido)
    if len(partidos_pais) != 0:
        for juego in partidos_pais:
            juego.ver_partido()
    else:
        print("\nNo se ha encontrado ningun partido con el equipo mencionado.")

def partido_estadio(lista_partidos):
    #Busca partidos por estadio
    name = input("Por favor indique el nombre del estadio: \n -> ")
    partidos_estadios = []
    for partido in lista_partidos:
        if partido.ver_estadios() == name:
            partidos_estadios.append(partido)
    if len(partidos_estadios) != 0:
        for juego in partidos_estadios:
            juego.ver_partido()
    else:
        print("\nNo se ha encontrado ningún partido relacionado con el estadio indicado \n ")

def partido_fecha(lista_partidos):
    #Busca partidos por fecha
    print("\nPor favor indique la fecha utilizando el siguiente formato:")
    date = input("YYYY-MM-DD \n \n -> ") #Buscar si esto está correcto!!!
    partidos_fecha = []
    for partido in lista_partidos:
        if partido.ver_fecha() == date:
            partidos_fecha.append(partido)
    if len(partidos_fecha) != 0:
        for juego in partidos_fecha:
            juego.ver_partido()
    else:
        print("\nNo se ha encontrado ningún partido con la fecha indicada \n ")
            


def buscar_partido(lista_partidos):
    #Menú principal de busqueda de partidos
    while True:
        print("\n---------------------------------")
        print("******Busqueda de Partidos******")
        print("---------------------------------")
        print("Indique cómo desea buscar los partidos:")
        print("1. Por país \n 2. Por estadio \n 3. Por fecha \n 4. Regresar")
        seleccion = input("-> ")
        if seleccion == "1":
            partido_pais(lista_partidos)
        elif seleccion == "2":
            partido_estadio(lista_partidos)
        elif seleccion == "3":
            partido_fecha(lista_partidos)
        elif seleccion == "4":
            break
        else:
            print("Se ha ingresado una opción inexistente. Intente de nuevo. \n ")
