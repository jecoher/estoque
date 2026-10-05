from logica import Producto, Inventario

inventario_completo = Inventario()
base_de_datos = "inventario.json"


try:
    inventario_completo.cargar_json(base_de_datos)
except FileNotFoundError:
    print("Iniciando con un inventario nuevo!")

while True:
    opc_menu = input("""
[1] Agregar porducto
[2] Mostra producto
[3] Buscar por ID
[4] Eliminar producto
[5] Vender producto
[6] Salir
: """).strip()
    if opc_menu == '5':
        print("Saliendo del sistema")
        break
    elif opc_menu == '1':
        id_prodcuto = inventario_completo.siguiente_id()
        nombre_producto = input("Digite el nombre del prodcuto: ").strip().upper()
        precio_producto = float(input("Digite  el precio del prodcuto: "))
        cantidad_producto = float(input("Digite la cantidad del prodcuto: "))

        producto_nuevo = Producto(id_prodcuto, nombre_producto, precio_producto, cantidad_producto)
        inventario_completo.agregar_producto(producto_nuevo)
        inventario_completo.guardar_json(base_de_datos)
        print(f"Producto {nombre_producto} adicionado con exito!")
    elif opc_menu == '2':
        if not inventario_completo.productos:
            print("inventario vacio!")
            continue
        else:
            for producto in inventario_completo.productos:
                    print(f"ID: {producto.id} | Nombre: {producto.nombre} | Precio: {producto.precio} | Cantidad: {producto.cantidad} |")
    elif opc_menu == '3':
        try:
            id_buscar = int(input("Digite el ID: "))
            producto_encontrado = inventario_completo.buscar_producto_por_id(id_buscar)
            if producto_encontrado is None:
                print("Producto no encontrado!")
                continue
            else:
                print(f"ID: {producto_encontrado.id} | Nombre: {producto_encontrado.nombre} | Precio: {producto_encontrado.precio} | Cantidad: {producto_encontrado.cantidad} |")
                continue
        except ValueError:
            print("valor id invalido!")    
    elif opc_menu == '4':
        id_eliminar = int(input("Digite el ID para eliminar: "))
        id_eliminado = inventario_completo.eliminar_producto_por_id(id_eliminar)
        if id_eliminado:
            print("Producto eliminado con exito!")
            inventario_completo.guardar_json(base_de_datos)
        else:
            print("Error: Producto no encontrado")
    elif opc_menu == '5':
        id_vender = int(input("Digite el ID: "))
        producto_encontrado = inventario_completo.buscar_producto_por_id(id_vender)
        if producto_encontrado is None:
            print("Producto no encontrado!")
        else:
            cantidad_vender = float(input("Digite cantidad a vender: "))
            valor_total = producto_encontrado.vender(cantidad_vender)
            if valor_total > 0:
                print(f"Venta exitosa | valor total: {valor_total:.2f}")
                inventario_completo.guardar_json(base_de_datos)
                continue
            else:
                print("Producto sin estoque suficiente!") 
                continue
    

