#En este archivo se define la clase Restaurante

class Restaurante:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
    
    def ver_productos(self):
        #Retorna la lista de productos
        return self.productos