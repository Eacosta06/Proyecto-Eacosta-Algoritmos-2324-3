#Este es el archivo main del programa

"""NOTA IMPORTANTE: La gestión de estadísticas es muy lenta. Si hubiera tenido más tiempo
hubiera utilizado insertion o quicksort

Por favor no utilice las estadisticas de productos más vendidos y partidos con más asistencia.
En serio, corralas en frío, se tardan medio año."""

import funcionesFiles as fF
import funcionesPartidos as fP
import funcionesEntradas as fE
import funcionesAsistencia as fA
import funcionesRestaurant as fR
import funcionesEstadisticas as fEs

def menu(estadios, equipos, partidos, clientes):
    #Esta función muestra el menú principal y ejecuta las funciones de cada módulo.
    while True:
        print("\n******Bienvenido al sistema de gestión Euro 2024****** \n ")
        print("Indique la opción a la que desea acceder: \n")
        print("1. Gestión de partidos y estadios \n2. Gestión de venta de entradas \n3. Gestión de asistencia a partidos")
        print("4. Gestión de restaurantes \n5. Gestión de venta de restaurantes \n6. Indicadores de gestión (Estadísticas) \n0. Salir")
        selection = input("-> ")
        if selection == "1":
            fP.buscar_partido(partidos)
        elif selection == "2":
            fE.comprar_ticket(clientes, partidos)
        elif selection == "3":
            fA.validar_entrada(clientes, partidos)
        elif selection == "4":
            fR.buscar_productos(estadios)
        elif selection == "5":
            fR.comprar_producto(estadios, clientes)
        elif selection == "6":
            fEs.estadisticas(clientes, estadios, equipos, partidos)
        elif selection == "0":
            print("\nHasta luego. Que tenga un feliz día.")
            print("\nCerrando... \n")
            fF.guardar_archivos(estadios, equipos, partidos, clientes)
            break
        else:
            print("\nSe ha introducido una opción incorrecta. Intentelo de nuevo.")

def main():
    #función main del proyecto.
    estadios, equipos, partidos, clientes = fF.abrir_archivos()
    menu(estadios, equipos, partidos, clientes)

main()