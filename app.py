import json

# FUNC VALIDACION, TRATAMIENTO, CARGA Y DESCAGAR
########################################################
def tratamiento_float(entrada_user):
    """
    devuelve float si el numero esta correcto
    None >>> si hay valor diferente de float
    """
    try:
        cambio_para_float = float(entrada_user)
        return cambio_para_float
    except ValueError:
        return None
    
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
    elif int_user == 'r':
        return 'r'
    else:
         return None

def validacion_id_user(id_user):
    try:
        id_validado = int(id_user)
        return id_validado
    except ValueError:
        return None

def verificar_ultimo_id_registrado(lista):
    if not lista:
        return 1
    else:
        id_exitente = [producto['id'] for producto in lista]
        mayor_id = max(id_exitente)
        return mayor_id + 1 

def guardar_datos(lista, nombre_archivo="productos.json"):
    with open(nombre_archivo, 'w', encoding="utf-8") as file:
        json.dump(lista, file, indent=4, ensure_ascii=False)

def cargar_datos(nombre_archivo='productos.json'):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# FUNC COMERCIALES
########################################################
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

def formatear_prodcuto_nuevo_para_dict(id, nombre, precio, cantidad): 
    """
    Devuelve un diccionario con las informaciones del producto, listas para su append
    """
    return {"id": id, "nombre": nombre, "precio": precio, "cantidad": cantidad}


# --------------
# LISTA DE PRODUCTOS
# --------------

lista_productos = cargar_datos()


# --------------
# MENU PRINCIPAL
# --------------

while True:
    opc_menu_principal_user = input("""
Que desea hacer: 
[v]ender
[e]liminar
[a]justar
[r]egistrar producto
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


        # ----------REGISTRO----------
    elif accion_user == 'r':
        id = verificar_ultimo_id_registrado(lista_productos)
        while True:
            nombre_prod_nuevo = input("Digite el nombre del producto: ").strip().upper()
            precio_prod_nuevo = tratamiento_float(input("Digite el precio del producto: "))
            if precio_prod_nuevo is None:
                print("Valor precio invalido!")
                break

            cantidad_prod_nuevo = tratamiento_float(input("DIgite la cantidad del producto: "))
            if cantidad_prod_nuevo is None:
                print("Valor cantidad invalido!")
                break
            producto_formateado = formatear_prodcuto_nuevo_para_dict(id, nombre_prod_nuevo, precio_prod_nuevo, cantidad_prod_nuevo)
            lista_productos.append(producto_formateado)
            print("Producto registrado con exito!")
            print(producto_formateado)
            guardar_datos(lista_productos)
            break
                
    else:
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
                    unidades_operacion = tratamiento_float(input("Digite una cantidad: "))

                    if unidades_operacion is None:
                        print("Digite una cantidad valida!")
                        continue
                    else:
                        if unidades_operacion > 0:
                            venta = vender_producto(producto_encontrado, unidades_operacion)
                            if venta is None:
                                print("Cantidad para venda menor que estoque!")
                                continue
                            else:
                                print(f"Venta realizada con exito, total a cobrar {venta}")
                                print(producto_encontrado)
                                guardar_datos(lista_productos)
                                continue
                        else:
                            print("Valor negativo invalido!")
                            continue


    # ----------ELIMINAR----------                    
                elif accion_user == 'e':
                    confirmacion_user = input("eliminar prodcuto: [s]i - [n]o: ")
                    if confirmacion_user == 's':
                        print(f"Producto Cod: {producto_encontrado['id']} - {producto_encontrado['nombre']} eliminado con exito")
                        lista_productos.remove(producto_encontrado)
                        guardar_datos(lista_productos)
                    elif confirmacion_user == 'n':
                        continue
                    else:
                        print("Opcion invalida!")

                    
    # ----------AJUSTE----------
                elif accion_user == 'a':
                        unidades_operacion_ajustar = tratamiento_float(input("Digite cantidad a ajustar: "))

                        if unidades_operacion_ajustar is None:
                                print("Digite una cantidad valida!")
                                continue

                        elif unidades_operacion_ajustar < 0:
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
                                guardar_datos(lista_productos)
                                continue
                            elif accion_ajuste_user == 's':
                                ajuste_salida = ajuste_producto(producto_encontrado, 's', unidades_operacion_ajustar)
                                
                                if ajuste_salida is None:
                                    print("Cantidad insuficiente!")
                                else:
                                    print("Ajuste de salida exitoso")
                                    print(producto_encontrado)
                                    guardar_datos(lista_productos)
                                    continue
                            else:
                                print("seleccion invalida!")
                                continue




                
