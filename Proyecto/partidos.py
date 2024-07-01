#En este archivo se define la clase Partido

class Partido:
    def __init__(self, id, num, eqL, eqV, fecha, estadio, grupo):
        self.id = id
        self.num = num
        self.equipoL = eqL
        self.equipoV = eqV
        self.fecha = fecha
        self.estadio = estadio
        self.grupo = grupo
        self.ticketsVIP = []
        self.ticketsG = []
    
    def ver_grupo(self):
        #Retorna el grupo del partido
        return self.grupo
    def ver_equipos(self):
        #Retorna los equipos que jugarán en el partido
        EquipoL = self.equipoL
        EquipoV = self.equipoV
        return EquipoL, EquipoV
    def ver_estadios(self):
        #Retorna el nombre del estadio asociado.
        return self.estadio.estadio_nombre()
    def ver_numero(self):
        #Retorna el número de partido.
        return self.num
    def ver_fecha(self):
        #Retorna la fecha.
        return self.fecha
    def ver_partido(self):
        #Muestra todos los datos del partido.
        print("----------------------------------")
        print(f"_____________Partido {self.num}____________")
        print("----------------------------------")
        codigoL = self.equipoL.equipo_code()
        codigoV = self.equipoV.equipo_code()
        print(f"\n     {codigoL} VS {codigoV}    ")
        print(f"Fecha: {self.fecha}")
        print(f"Grupo: {self.grupo}")
        print(f"Estadio: {self.estadio.estadio_nombre()} \n \n ")

    def estadios(self):
        #Retorna el ID del estadio asociado
        return self.estadio
    def verificar_VIP(self, seleccion):
        #Verifica si un ticket VIP ya existe
        if len(self.ticketsVIP) != 0:
            for ticket in self.ticketsVIP:
                if ticket == seleccion:
                    return False
            return True
        else:
            return True
    def verificar_General(self, seleccion):
        #Verifica si un ticket General ya existe
        if len(self.ticketsG) != 0:
            for ticket in self.ticketsG:
                if ticket == seleccion:
                    return False
            return True
        else:
            return True
    def añadir_VIP(self, seleccion):
        #añade el ID de un ticket VIP
        self.ticketsVIP.append(seleccion)
    def añadir_General(self, seleccion):
        #añade el ID de un ticket General
        self.ticketsG.append(seleccion)
