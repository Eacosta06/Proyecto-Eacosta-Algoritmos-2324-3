"""En este archivo se encuentran las funciones relacionadas al modulo
de gestión de asistencia y autenticidad de entradas."""

def buscar_entrada(partido, tipo, asiento):
    """Esta función verifica que el asiento indicado esté registrado
    dentro del objeto del partido"""
    if tipo == "Gen":
        if partido.verificar_General(asiento) == False:
            return True
        else:
            return False
    else:
        if partido.verificar_VIP(asiento) == False:
            return True
        else:
            return False

def modificar_entrada(clientes, codigo):
    """Esta función busca la entrada ingresada entre la lista de clientes,
    y modifica la asistencia a True"""
    for cliente in clientes:
        for ticket in cliente.mostrar_tickets():
            if ticket.ver_codigo() == codigo and ticket.ver_asistencia() == False:
                ticket.modificar_asistencia()
                print("\nSe ha modificado la asistencia del ticket ingresado.\n")
            elif ticket.ver_codigo() == codigo and ticket.ver_asistencia():
                print("\nEl ticket ingresado ya ha sido utilizado.\n")

def validar_entrada(clientes, partidos):
    """Esta función pregunta por el código a buscar, evalúa si tiene la estructura adecuada y
    la divide en varias partes para definir el partido al que pertenece, el tipo y el asiento."""
    while True:
        codigo = input("\nIngrese el código del ticket a validar: \n Escriba \"exit\" para salir \n -> ")
        if codigo == "exit":
            break
        try:
            lista = codigo.split("_")
            num = int(lista[0])
            asiento = int(lista[1])
            tipo = lista[2]
            v = False
            for partido in partidos:
                numero = partido.ver_numero()
                if numero == num:
                    if buscar_entrada(partido, tipo, asiento):
                        modificar_entrada(clientes, codigo)
                        v = True
            if not v:        
                print("\nLa entrada proporcionada no existe en la base de datos.")
        except:
            """Si la estructura ingresada es incorrecta se corre este print"""
            print("El codigo introducido no es un código válido.")
