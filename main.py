from logica import Producto, Inventario

inventario_completo = Inventario()

try:
    inventario_completo.cargar_json("inventario.json")
except FileNotFoundError:
    print("Iniciando con un inventario nuevo!")

while True:
    opc_menu = input("""
[1] Agregar porducto
[2] Mostra producucto
[3] Salir
: """).strip()
    if opc_menu == '3':
        id_prodcuto = inventario_completo.siguiente_id()
        nombre_producto = input("Digite le nombre del prodcuto: ").strip().upper()
        precio_producto = float(input("Digite le nombre del prodcuto: "))
        cantidad_producto = float(input("Digite le nombre del prodcuto: "))

        produto_nuevo = id_prodcuto, nombre_producto, precio_producto, cantidad_producto
        inventario_completo.agregar_producto(prodcuto_nuevo)
    elif opc_menu == '1':
        pass
    elif opc_menu == '2':
        pass