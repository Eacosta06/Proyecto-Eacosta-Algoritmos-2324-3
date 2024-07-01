#En este archivo se define la clase Equipo

class Equipo:
    def __init__(self, nombre, ID, codigo, grupo):
        self.nombre = nombre
        self.id = ID
        self.codigo = codigo
        self.grupo = grupo
        self.entradas = [0, 0]
    
    def equipo_id(self):
        #Retorna el ID del equipo
        return self.id
    def equipo_code(self):
        #Retorna el código del equipo
        return self.codigo
    def ver_nombre(self):
        #Retorna el nombre del equipo (El país)
        pais = self.nombre
        return pais