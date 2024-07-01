#En este archivo se encuentra definida la clase de las entradas

class Entrada:
    def __init__(self, codigo):
        self.codigo = codigo
        self.asistencia = False
        self.VIP = False
    
    def modificar_asistencia(self):
        #Modifica la asistencia a True
        self.asistencia = True
    def ver_vip(self):
        #Retorna el valor VIP
        return self.VIP
    def ver_codigo(self):
        #Retorna el ID
        return self.codigo
    def ver_asistencia(self):
        #Retorna la asistencia
        return self.asistencia


class EntradaVIP(Entrada):
    def __init__(self, codigo):
        super().__init__(codigo)
        self.VIP = True
        self.asistencia = False