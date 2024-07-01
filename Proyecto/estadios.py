#En este archivo se define la clase Estadio

class Estadio:
    def __init__(self, nombre, id, ubicacion, capacidadG, capacidadVIP, restaurantes):
        self.nombre = nombre
        self.id = id
        self.ubicacion = ubicacion
        self.capacidadG = capacidadG
        self.capacidadVIP = capacidadVIP
        self.restaurants = restaurantes
    
    def buscar_id(self):
        #Retorna el ID del estadio
        return self.id
    def estadio_nombre(self):
        #Retorna el nombre del estadio
        return self.nombre
    def ver_asientosVIP(self):
        #Retorna una matriz 10xN con los asientos VIP
        for fila in self.capacidadVIP:
            for asiento in fila:
                print(asiento, end= " ")
            print("\n")
    def ver_asientosGen(self):
        #Retorna una matriz 10xN con los asientos Generales
        for fila in self.capacidadG:
            for asiento in fila:
                print(asiento, end= " ")
            print("\n")
    def existe_VIP(self, seleccion):
        #Verifica la existencia de un asiento VIP
        for fila in self.capacidadVIP:
            for asiento in fila:
                if asiento == seleccion:
                    return True
        return False
    def existe_General(self, seleccion):
        #Verifica la existencia de un asiento VIP
        for fila in self.capacidadG:
            for asiento in fila:
                if asiento == seleccion:
                    return True
        return False
    
    def ver_restaurants(self):
        #Retorna la lista de restaurantes
        return self.restaurants