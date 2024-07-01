
import funcionesEstadisticas as fE
import funcionesEntradas as fT

def lista_productos(estadios):
    #Crea una lista de productos desde los estadios
    productos = []
    for estadio in estadios:
        for restaurant in estadio.ver_restaurants():
            for producto in restaurant.ver_productos():
                productos.append(producto)
    return productos

def buscar_nombre(productos):
    #Busca productos por su nombre
    nombre = input("\nIngrese el nombre del producto a buscar: \n-> ")
    for producto in productos:
        if producto.ver_nombre() == nombre:
            print(producto.ver_producto(1))

def buscar_tipo(productos, tipo):
    #Busca productos por su tipo
    for producto in productos:
        if producto.ver_adicional() == tipo:
            print(producto.ver_producto(1))

def que_tipo(productos):
    #Pregunta que tipo de producto se quiere
    print("\n¿Que tipo de producto desea buscar?:")
    seleccion = input(" 1. Bebida \n 2. Comida \n-> ")
    if seleccion == "1":
        print("---------------------")
        tipo = input(" 1. No Alcoholica \n 2. Alcoholica \n-> ")
        if tipo == "1":
            buscar_tipo(productos, "non-alcoholic")
        elif tipo == "2":
            buscar_tipo(productos, "alcoholic")
        else:
            print("Se ha introducido un valor inválido. Intentelo de nuevo.")
    elif seleccion == "2":
        print("---------------------")
        tipo = input(" 1. De paquete \n 2. Plato \n-> ")
        if tipo == "1":
            buscar_tipo(productos, "package")
        elif tipo == "2":
            buscar_tipo(productos, "plate")
        else:
            print("Se ha introducido un valor inválido. Intentelo de nuevo.")
    else:
        print("Se ha introducido un valor inválido. Intentelo de nuevo.")


def buscar_precio(productos, min, max):
    #Busca los productos en un rango de precio
    for producto in productos:
        precio = producto.ver_precio()
        if precio >= min and precio <= max:
            producto.ver_producto(1)

def rango_precio(productos):
    #Pregunta un rango de precio
    print("\n Los precios se buscan con el Iva incluido. \n")
    min = input("\nIndique el precio mínimo: \n ->")
    if fT.numerico(min):
        min = int(min)
        max = input("Indique el precio máximo: \n ->")
        if fT.numerico(max) and int(max) > min:
            max = int(max)
            buscar_precio(productos, min, max)
        elif int(max) < min:
            print("\n El máximo no puede ser un número menor al mínimo. Intentelo de nuevo.")
        else:
            print("\n Se ha ingresado un valor incorrecto. \n Porfavor ingrese el precio como número entero.")
    else:
        print("\n Se ha ingresado un valor incorrecto. \n Porfavor ingrese el precio como número entero.")

def buscar_productos(estadios):
    #Menú principal de busqueda de productos
    productos = lista_productos(estadios)
    while True:
        print("\n******Gestión de Restaurantes******")
        print("\n¿Cómo desea buscar los productos?: \n 1. Por nombre \n 2. Por tipo \n 3. Por precio \n exit - Regresar")
        seleccion = input("-> ")
        if seleccion == "1":
            buscar_nombre(productos)
        elif seleccion == "2":
            que_tipo(productos)
        elif seleccion == "3":
            rango_precio(productos)
        elif seleccion == "exit":
            break
        else:
            print("\nSe ha ingresado un valor inválido. Intentelo de nuevo.")

def verificar_vip(cliente):
    #Verifica el VIP de un cliente
    for ticket in cliente.mostrar_tickets():
        if ticket.ver_vip():
            return True
    return False

def buscar_cliente(clientes, cedula):
    #Busca un cliente
    for cliente in clientes:
        if cliente.ver_cedula() == cedula:
            if verificar_vip(cliente):
                return cliente
            else:
                print("\nAcceso Denegado. \nEl cliente no tiene acceso VIP.")
                return False
    print("\nEl cliente no ha comprado ningún asiento y/o no ha sido registrado.")


def numero_perfecto(cedula):
    #Verifica si la cedula es un numero perfecto
    str_cedula = str(cedula)
    divisores = []
    n = 1
    while n < cedula:
        if cedula % (n) == 0:
            divisores.append(n)
        n += 1
    suma = 0
    for num in divisores:
        suma += num
    if suma == cedula:
        print("\nSu cedula es un numero perfecto y ha recibido un descuento del 30%.")
        return 0.3
    else:
        return 1

def completar_compra(producto, cliente, descuento):
    #Pregunta para finalizar la compra
    producto.ver_producto(descuento)
    seleccion = input("\n¿Completar la compra?: \n 1. Si \n 2. No\n -> ")
    if seleccion == "1":
        cliente.anadir_producto(producto.ver_nombre())
        producto.modificar_stock()
        print("\nProcesando compra...")
        print("Compra finalizada. Muchas Gracias.")
    elif seleccion == "2":
        print("\n Cancelando compra... \n")
    else:
        print("Se ha ingresado una opción inválida. Intentelo de nuevo.")


def comprar_productos(cliente, productos):
    #Verifica la existencia de los productos.
    while True:
        v = False
        nombre = input("\nIngrese el nombre del producto que desea comprar: \nEscriba \"return\" para regresar\n-> ")
        if nombre == "return":
            break
        elif cliente.ver_edad() >= 18:
            for producto in productos:
                if producto.ver_nombre() == nombre and producto.ver_stock() != 0:
                    descuento = numero_perfecto(cliente.ver_cedula())
                    completar_compra(producto, cliente, descuento)
                    v = True
                    break
                elif producto.ver_nombre() == nombre and producto.ver_stock() == 0:
                    print("\nEl producto se encuentra fuera de stock.")
                    break
            if not v:
                print("\nNo se ha encontrado ningún producto con el nombre ingresado. Intentelo de nuevo.")

        elif cliente.ver_edad() < 18:
            #COMPLETAR PARA MENOR A 18!!!
            for producto in productos:
                if producto.ver_nombre() == nombre and producto.ver_stock() != 0:
                    if producto.ver_adicional() != "alcoholic":
                        descuento = numero_perfecto(cliente.ver_cedula())
                        completar_compra(producto, cliente, descuento)
                        v = True
                        break
                    else:
                        print("\nSu edad no cumple el requisito mínimo para comprar productos alcoholicos.")
                        v= True
                        break
                elif producto.ver_nombre() == nombre and producto.ver_stock() == 0:
                    print("\nEl producto se encuentra fuera de stock.")
            if not v:
                print("\nNo se ha encontrado ningún producto con el nombre ingresado. Intentelo de nuevo.")


def comprar_producto(estadios, clientes):
    #Menu principal de compra de productos
    productos = lista_productos(estadios)
    while True:
        print("\n******Compra de productos******")
        cedula = input("\nPorfavor ingrese su numero de cedula: \nEscriba \"exit\" para regresar \n -> ")
        if cedula != "exit":
            if fT.numerico(cedula):
                cedula = int(cedula)
                if buscar_cliente(clientes, cedula):
                    cliente = buscar_cliente(clientes, cedula)
                    comprar_productos(cliente, productos)
            else:
                print("\nSe ha ingresado un valor incorrecto. \n Recuerde que la cédula debe ser un valor numérico.")
        else:
            break
            