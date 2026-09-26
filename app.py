lista_productos = [
    {"id": 1, "nombre": "ESCOBA", "precio": 15.0, "cantidad": 10},
    {"id": 2, "nombre": "ESPONJA", "precio": 5.0, "cantidad": 50},
]

def buscar_prodcuto_por_id(lista, id_busca):
    """
    none -> si no encuentra producto\n
    producto -> si lo encuentra
    """
    for producto in lista:
        if producto['id'] == id_busca:
            return producto
    return None

def eliminar_producto_por_id(lista, id_eliminar):
    """
    True -> producto eliminado\n
    False -> producto no encontrado
    """
    producto_encontrado = buscar_prodcuto_por_id(lista, id_eliminar)
    if producto_encontrado is None:
        return False
    else:
        lista.remove(producto_encontrado)
        return True
        
def vender_producto(lista, id_vender, cantidad):
    """
    None -> producto no encontrado\n
    False -> cantidad producto menor a solicitada\n
    Float con valor total a cobrar
    """ 
    producto_encontrado = buscar_prodcuto_por_id(lista, id_vender)
    if producto_encontrado is None:
        return None
    elif producto_encontrado['cantidad'] < cantidad:
        return False

    else:
        producto_encontrado['cantidad'] -= cantidad
        total_cobrar = producto_encontrado['precio'] * cantidad
        return float(total_cobrar)

def reabastecer_con_id(lista, id_reavastecer, cantidad):
    producto_encontrado = pro


id_objetivo = 51
accion = "eliminar"        
unidades_operacion = 4

producto_encontrado = buscar_prodcuto_por_id(lista_productos, id_objetivo)

if accion == 'vender':
    venta = vender_producto(lista_productos, id_objetivo, unidades_operacion)
    if venta is None:
        print("Producto no encontrado!")
    elif venta is False:
        print("Cantidad para venda menor que estoque!")
    else:
        print(f"Venta realizada con exito, total a cobrar {venta}")


elif accion == 'reabastecer':
    producto_encontrado['cantidad'] += unidades_operacion
    print(f"Fueron adicionados para cod {producto_encontrado['id']} {producto_encontrado['nombre']} {unidades_operacion} unidades. Ahora tiene {producto_encontrado['cantidad']} unidades")


elif accion == "eliminar":
    eliminar = eliminar_producto_por_id(lista_productos, id_objetivo)
    if eliminar:
        print(f"Prodcuto eliminado con exito!")
        print(lista_productos)
    else:
        print("prodcuto no encontrado")

