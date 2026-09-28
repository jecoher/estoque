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

def verificar_ultimo_id_registrado(lista):
    if not lista:
        return 1
    else:
        id_exitente = [producto['id'] for producto in lista]
        mayor_id = max(id_exitente)
        return mayor_id + 1 