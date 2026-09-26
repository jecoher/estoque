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
    producto_encontrado = buscar_prodcuto_por_id(lista, id_reavastecer)
    if producto_encontrado is None:
        return None
    else:
        producto_encontrado["cantidad"] += cantidad
        return producto_encontrado


id_objetivo = 1
accion = "reabastecer"        
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
    
    reabastecer = reabastecer_con_id(lista_productos, id_objetivo, unidades_operacion)
    if reabastecer is None:
        print("Producto no encontrado!")
    else:
        print("prodcuto reabastecido con exito!")
        print(f"Fueron adicionados para cod {reabastecer['id']} {reabastecer['nombre']} {unidades_operacion} unidades. Ahora tiene {reabastecer['cantidad']} unidades")
        print(reabastecer)

elif accion == "eliminar":
    eliminar = eliminar_producto_por_id(lista_productos, id_objetivo)
    if eliminar:
        print(f"Prodcuto eliminado con exito!")
        print(lista_productos)
    else:
        print("prodcuto no encontrado")

