lista_productos = [
    {"id": 1, "nombre": "ESCOBA", "precio": 15.0, "cantidad": 10},
    {"id": 2, "nombre": "ESPONJA", "precio": 5.0, "cantidad": 50},
]

def validar_opcion_menu(int_user):
    """
    Devuelve la opc del menu principal\n
    None -> si no es ninguna de las seleccionadads
    """
    if int_user == "v":
        return 'v'
    elif int_user == "e":
            return 'e'
    elif int_user == "a":
            return 'a'
    elif int_user == "s":
            return 's'
    else:
         return None

def validacion_id_user(id_user):
    try:
        id_validado = int(id_user)
        return id_validado
    except ValueError:
        return None

def buscar_prodcuto_por_id(lista, id_busca):
    """
    -> Devuelve el diccionario encontrado\n
    None -> si no encuentra producto\n
    """
    for producto in lista:
        if producto['id'] == id_busca:
            return producto
    return None

def vender_producto(diciconario_producto, cantidad):
    """
    -> Devuelve el valor total a cobrar\n
    False -> cantidad producto menor a solicitada\n
    Float con valor total a cobrar
    """ 
    if diciconario_producto['cantidad'] < cantidad:
        return None

    else:
        diciconario_producto['cantidad'] -= cantidad
        total_cobrar = diciconario_producto['precio'] * cantidad
        return float(total_cobrar)

def ajuste_producto(diccionario, tipo_ajuste, cantidad):
    """
    ->  Devuelve cantidad actualizada ajustada (entrad/salida)\n
    None -> si no es entrada o salida
    False -> no es e ni s
    nones si es menor catidad a sacar que cantidad de producto
    """
    if tipo_ajuste == 'e':
        diccionario['cantidad'] += cantidad
        return diccionario['cantidad']
    elif tipo_ajuste == 's':
        if diccionario['cantidad'] < cantidad:
            return None
        else:
            diccionario['cantidad'] -= cantidad
            return diccionario['cantidad']
    else:
        return None
        





# --------------
# MENU PRINCIPAL
# --------------

while True:
    opc_menu_principal_user = input("""
Que desea hacer: 
[v]ender
[e]liminar
[a]justar
[s]salir
: """).strip().lower()

    accion_user = validar_opcion_menu(opc_menu_principal_user) 

    if accion_user is None:
        print('Opcion invalida!')
        continue

        # ----------SALIR----------
    elif accion_user == 's':
        print("saliendo del sistema!")
        break


    id_objetivo = input("Digite el ID del producto : ")
    validacion_id = validacion_id_user(id_objetivo)
    if validacion_id is None:
        print("Digite un id valido!")
        continue
    else:
        # ----------producto encontrado----------
        producto_encontrado = buscar_prodcuto_por_id(lista_productos, validacion_id)

        if producto_encontrado is None:
            print("Producto no encontrado")
            continue
        else:
            print(producto_encontrado)


# ----------VENDER----------
            if accion_user == 'v':
                try:
                    unidades_operacion = float(input("Digite la cantidad: "))
                except ValueError:
                    print("Digite un valor valido!")
                    continue

                if unidades_operacion > 0:
                    venta = vender_producto(producto_encontrado, unidades_operacion)
                    if venta is None:
                        print("Cantidad para venda menor que estoque!")
                        continue
                    else:
                        print(f"Venta realizada con exito, total a cobrar {venta}")
                        print(producto_encontrado)
                        continue
                else:
                    print("cantidad invalida!")


# ----------ELIMINAR----------                    
            elif accion_user == 'e':
                confirmacion_user = input("eliminar prodcuto: [s]i - [n]o: ")
                if confirmacion_user == 's':
                    print(f"Producto Cod: {producto_encontrado['id']} - {producto_encontrado['nombre']} eliminado con exito")
                    lista_productos.remove(producto_encontrado)
                elif confirmacion_user == 'n':
                    continue
                else:
                    print("Opcion invalida!")

                
# ----------AJUSTE----------
            elif accion_user == 'a':
                    try:
                        unidades_operacion_ajustar = float(input("Digite la cantidad a ajustar: "))
                    except ValueError:
                        print("Digite una cantidad valida!")
                        continue

                    if unidades_operacion_ajustar < 0:
                        print('Cantidad invalida!')
                    else:

                        accion_ajuste_user = input("""
    [e]ntrada
    [s]alida
    : """).strip().lower()
                        if accion_ajuste_user == 'e':
                            ajuste_producto(producto_encontrado, 'e', unidades_operacion_ajustar)
                            print("Ajuste de entrada exitoso")
                            print(producto_encontrado)
                            continue
                        elif accion_ajuste_user == 's':
                            ajuste_salida = ajuste_producto(producto_encontrado, 's', unidades_operacion_ajustar)
                            
                            if ajuste_salida is None:
                                print("Cantidad insuficiente!")
                            else:
                                print("Ajuste de salida exitoso")
                                print(producto_encontrado)
                                continue
                        else:
                            print("seleccion invalida!")
                            continue
