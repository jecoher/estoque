lista_productos = []

def consecutivo_id(lista):
    return len(lista) + 1

def validacion_valores_num_producto(opcion_usuario):
    '''
    valida si la opcion digitada por usuario no es negativa ni un espacio en blanco o una str.
    '''
    try: 
        opcion_usuario_float = float(opcion_usuario)
        if opcion_usuario_float < 0:
            return None
        return opcion_usuario_float
    except ValueError:
        return(None)
    
def validacion_int_user(opcion_usuario):
    '''
    valida si la opcion digitada por usuario no es negativa ni un espacio en blanco o una str.
    '''
    try: 
        opcion_usuario_int = int(opcion_usuario)
        if opcion_usuario_int < 0:
            return None
        return opcion_usuario_int
    except ValueError:
        return(None)

    
while True:

    opc_menu_user = input("""
[1] Registrar producto
[2] Buscar producto
[3] Salir
: """).strip()

    if opc_menu_user == '1':
        numero_id = consecutivo_id(lista_productos)
        while True:
            nombre = input("Digite el nombre del producto: ").strip().upper()
            if nombre == "":
                print("Valor vacio, Invalido!")
                continue
            break

        while True:
            precio = input("Digite el precio del producto: R$").strip()
            precio_verificado = validacion_valores_num_producto(precio)
            if precio_verificado is None:
                print("Valor invalido!")
                continue
            break

        while True:
            cantidad = input("Digite la cantidad del producto: ").strip()
            cantidad_verificado = validacion_valores_num_producto(cantidad)
            if cantidad_verificado is None:
                print("Valor invalido!")
                continue
            break

        lista_productos.append({"id":numero_id, "nombre":nombre, "precio":precio_verificado, "cantidad": cantidad_verificado})
        print("Producto adicionado con exito")
        print(lista_productos)


    elif opc_menu_user == '2':
        usuario_produto = input('Digite el ID del producto a buscar: ').strip()
        usuario_produto_verificado = validacion_int_user(usuario_produto)
        if usuario_produto_verificado is None:
            print("Digite un id valido!")
            continue

        if len(lista_productos) < 1:
            print("Lista vacia!")
            continue

        else:
            for producto in lista_productos:
                if producto['id'] == usuario_produto_verificado:
                    print(producto)
            else:
                print("Producto no encontrado!")
    elif opc_menu_user == '3':
        print("Saliendo del sistema!")
        break
    else:
        print("Opcion Invalida!")