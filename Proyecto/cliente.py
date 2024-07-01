#En este archivo se define el objeto cliente y sus herencias

class Cliente:
    def __init__(self, nombre, ci, edad):
        self.nombre = nombre
        self.cedula = ci
        self.edad = edad
        self.tickets = []
        self.productos = []
    
    def anadir_ticket(self, ticket):
        #añade un ticket
        self.tickets.append(ticket)
    def anadir_producto(self, producto):
        #añade el nombre de un producto
        self.productos.append(producto)
    def mostrar_tickets(self):
        #Retorna la lista de tickets
        return self.tickets
    def ver_cedula(self):
        #Retorna la cedula del cliente
        return self.cedula
    def ver_nombre(self):
        #Retorna el nombre del cliente
        return self.nombre
    def ver_edad(self):
        #Retorna la edad del cliente
        return self.edad
    def ver_productos(self):
        #Retorna la lista de productos
        return self.productos

