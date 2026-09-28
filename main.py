import persistencia
import validaciones
import logica


# --------------
# LISTA DE PRODUCTOS
# --------------

lista_productos = persistencia.cargar_datos()


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
    accion_user = validaciones.validar_opcion_menu(opc_menu_principal_user) 
    if accion_user is None:
        print('Opcion invalida!')
        continue


        # ----------SALIR----------
    elif accion_user == 's':
        print("saliendo del sistema!")
        break


        # ----------REGISTRO----------
    elif accion_user == 'r':
        id = logica.verificar_ultimo_id_registrado(lista_productos)
        while True:
            nombre_prod_nuevo = input("Digite el nombre del producto: ").strip().upper()
            precio_prod_nuevo = validaciones.tratamiento_float(input("Digite el precio del producto: "))
            if precio_prod_nuevo is None:
                print("Valor precio invalido!")
                break

            cantidad_prod_nuevo = validaciones.tratamiento_float(input("DIgite la cantidad del producto: "))
            if cantidad_prod_nuevo is None:
                print("Valor cantidad invalido!")
                break
            producto_formateado = logica.formatear_prodcuto_nuevo_para_dict(id, nombre_prod_nuevo, precio_prod_nuevo, cantidad_prod_nuevo)
            lista_productos.append(producto_formateado)
            print("Producto registrado con exito!")
            print(producto_formateado)
            persistencia.guardar_datos(lista_productos)
            break
                
    else:
        id_objetivo = input("Digite el ID del producto : ")
        validacion_id = validaciones.validacion_id_user(id_objetivo)
        if validacion_id is None:
            print("Digite un id valido!")
            continue
        else:
            # ----------producto encontrado----------
            producto_encontrado = logica.buscar_prodcuto_por_id(lista_productos, validacion_id)

            if producto_encontrado is None:
                print("Producto no encontrado")
                continue
            else:
                print(producto_encontrado)


    # ----------VENDER----------
                if accion_user == 'v':
                    unidades_operacion = validaciones.tratamiento_float(input("Digite una cantidad: "))

                    if unidades_operacion is None:
                        print("Digite una cantidad valida!")
                        continue
                    else:
                        if unidades_operacion > 0:
                            venta = logica.vender_producto(producto_encontrado, unidades_operacion)
                            if venta is None:
                                print("Cantidad para venda menor que estoque!")
                                continue
                            else:
                                print(f"Venta realizada con exito, total a cobrar {venta}")
                                print(producto_encontrado)
                                persistencia.guardar_datos(lista_productos)
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
                        persistencia.guardar_datos(lista_productos)
                    elif confirmacion_user == 'n':
                        continue
                    else:
                        print("Opcion invalida!")

                    
    # ----------AJUSTE----------
                elif accion_user == 'a':
                        unidades_operacion_ajustar = validaciones.tratamiento_float(input("Digite cantidad a ajustar: "))

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
                                logica.ajuste_producto(producto_encontrado, 'e', unidades_operacion_ajustar)
                                print("Ajuste de entrada exitoso")
                                print(producto_encontrado)
                                persistencia.guardar_datos(lista_productos)
                                continue
                            elif accion_ajuste_user == 's':
                                ajuste_salida = logica.ajuste_producto(producto_encontrado, 's', unidades_operacion_ajustar)
                                
                                if ajuste_salida is None:
                                    print("Cantidad insuficiente!")
                                else:
                                    print("Ajuste de salida exitoso")
                                    print(producto_encontrado)
                                    persistencia.guardar_datos(lista_productos)
                                    continue
                            else:
                                print("seleccion invalida!")
                                continue




                
