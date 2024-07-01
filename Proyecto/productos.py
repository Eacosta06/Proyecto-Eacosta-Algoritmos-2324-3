#En este archivo se define la clase Producto

import funcionesEstadisticas as fE
import funcionesRestaurant as fR

class Producto:
    def __init__(self, nombre, cantidad, precio, stock):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.stock = stock
        self.adicional = None
    
    def modificar_stock(self):
        #modifica el stock y la cantidad por 1
        self.stock -= 1
        self.cantidad += 1
    def ver_nombre(self):
        #Retorna el nombredel producto
        return self.nombre
    def ver_producto(self, descuento):
        #Muestra los detalles del producto
        precio = float(self.precio)
        print("\n-------------------------------------------------------")
        print(f"_____________{self.nombre}____________")
        print("-------------------------------------------------------\n \n \n")
        print(f"\n \n \n{self.nombre}:                      {precio}")
        if descuento != 1:
            Iva = fE.IVA(precio - (precio*descuento))
            print(f"Descuento:                      {descuento*100}")
            print(f"\n \n \nSubtotal:                      {precio - (precio*descuento)}")
            print(f"Iva:                           {Iva}")
            print("--------------------------------------")
            print(f"Total:                        {float(precio - (precio*descuento)) + Iva}\n")
        else:
            Iva = fE.IVA(precio)
            print(f"\n \n \nSubtotal:                      {precio}")
            print(f"Iva:                           {Iva}")
            print("--------------------------------------")
            print(f"Total:                        {float(precio - (precio*descuento)) + Iva}\n")
        

    def ver_adicional(self):
        #Retorna el adicional
        return self.adicional
    def ver_precio(self):
        #Retorna el precio + IVA
        return float(self.precio)+fE.IVA(self.precio)
    def ver_stock(self):
        #Retorna el Stock
        return self.stock
    def ver_cantidad(self):
        #Retorna la cantidad
        return self.cantidad

class BebidaAchl(Producto):
    def __init__(self, nombre, cantidad, precio, stock):
        super().__init__(nombre, cantidad, precio, stock)
        self.adicional = "alcoholic"

class Bebida(Producto):
    def __init__(self, nombre, cantidad, precio, stock):
        super().__init__(nombre, cantidad, precio, stock)
        self.adicional = "non-alcoholic"

class Comida(Producto):
    def __init__(self, nombre, cantidad, precio, stock, adicional):
        super().__init__(nombre, cantidad, precio, stock)
        self.adicional = adicional