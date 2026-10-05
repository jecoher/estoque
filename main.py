from logica import Producto, Inventario

inventario_completo = Inventario()

while True:
    opc_menu = input("""
[1] Agregar porducto
[2] Mostra producto
[3] Buscar por ID
[4] Eliminar producto
[5] Vender producto
[6] Salir
: """).strip()
    if opc_menu == '6':
        print("Saliendo del sistema")
        break
    elif opc_menu == '1':
        try:
            nombre_producto = input("Digite el nombre del prodcuto: ").strip().upper()
            precio_producto = float(input("Digite  el precio del prodcuto: "))
            cantidad_producto = float(input("Digite la cantidad del prodcuto: "))

            producto_nuevo = Producto(0, nombre_producto, precio_producto, cantidad_producto)
            inventario_completo.agregar_producto(producto_nuevo)
            print(f"Producto {nombre_producto} adicionado con exito!")
        except ValueError:
            print("Valor incorrecto!")
    elif opc_menu == '2':
        inventario_db = inventario_completo.obtener_todos_los_productos()
        if not inventario_db:
            print("Sin productos registrados!")
            continue
        else:
            for fila in inventario_db:
                id_prod = fila[0]
                nombre =  fila[1]
                cantidad = fila[2]
                precio = fila[3]
                print(f"ID: {id_prod} |NOMBRE: {nombre}  |CANTIDAD: {cantidad}  |PRECIO: {precio}")

    elif opc_menu == '3':
        try:
            id_buscar = int(input("Digite el iD a buscar: "))
            encontrado = inventario_completo.buscar_producto_por_id(id_buscar)
            if not encontrado:
                print("Producto no econtrado!")
                continue
            else:
                producto = encontrado[0]
                # for fila in encontrado:
                #     id_prod = fila[0]
                #     nombre =  fila[1]
                #     cantidad = fila[2]
                #     precio = fila[3]
                print(f"ID: {producto[0]} |NOMBRE: {producto[1]}  |CANTIDAD: {producto[2]}  |PRECIO: {producto[3]}")

        except ValueError:
            print("Digite un id valido!")

    elif opc_menu == '4':
        try:
            id_eliminar = int(input("Digite el iD a eliminar: "))
            encontrado = inventario_completo.buscar_producto_por_id(id_eliminar)
            if not encontrado:
                print("Producto no existe!")
                continue
            else:
                inventario_completo.eliminar_producto(id_eliminar)
                print("producto eliminado con exito!")
        except ValueError:     
            print("Digite un id valido!")

