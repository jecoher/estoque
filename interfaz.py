import tkinter as tk
from tkinter import ttk
from logica import Inventario, Producto

def guardar_datos():
    try:
        nombre = caja_guardar_nombre.get().strip().upper()
        cantidad = float(caja_guardar_cantidad.get())
        precio = float(caja_guardar_precio.get())

        nuevo_prod = Producto(0, nombre, cantidad, precio)
        mi_inventario.agregar_producto(nuevo_prod)
        etiqueta_confirmacion.config(text=f"{nombre} guardado con exito", fg="green")

        # --- TRUCO PRO: Limpiar las cajas para el siguiente producto ---
        caja_guardar_nombre.delete(0, tk.END)
        caja_guardar_cantidad.delete(0, tk.END)
        caja_guardar_precio.delete(0, tk.END)
    except ValueError:
        etiqueta_confirmacion.config(text="Error! escribe numeros validos", fg="red")

def mostrar_datos():
    # 1. Limpiar la tabla primero (borramos todos los "hijos" de la tabla)
    for fila in tabla_productos.get_children():
        tabla_productos.delete(fila)

    registros = mi_inventario.obtener_todos_los_productos()

    for fila in registros:
        tabla_productos.insert("", tk.END, values=fila)

def abrir_ventana_venta():
    ventana_venta = tk.Toplevel(ventana)
    ventana_venta.title("Vender producto")
    ventana_venta.geometry("300x500")

    tk.Label(ventana_venta, text="ID venta", font=("Arial", 14, "bold")).pack(pady=10)

    caja_id_venta = tk.Entry(ventana_venta)
    caja_id_venta.pack()

    tk.Label(ventana_venta, text="Cantidad a vender",  font=("Arial", 14, "bold")).pack(pady=10)
    caja_cantidad_venta = tk.Entry(ventana_venta)
    caja_cantidad_venta.pack(pady=10)

    etiqueta_mesaje_venta = tk.Label(ventana_venta, text="")
    etiqueta_mesaje_venta.pack()

    def confirmar_venta():
        try:
            id_venta = int(caja_id_venta.get())
            producto_a_vender = mi_inventario.buscar_producto_por_id(id_venta)
            if not producto_a_vender:
                etiqueta_mesaje_venta.config(text="Prodcuto no encontrado!", fg="blue")
            else:
                producto = producto_a_vender[0]
                cantidad_a_vender = float(caja_cantidad_venta.get())
                if producto[2] >= cantidad_a_vender:
                    nueva_cantidad = producto[2] - cantidad_a_vender
                    mi_inventario.vender_producto(id_venta, nueva_cantidad)
                    etiqueta_mesaje_venta.config(text="Venta Exitosa!", fg="green") 
                    mostrar_datos()
                else:
                   etiqueta_mesaje_venta.config(text="Cantidad insuficiente!", fg="orange") 

        except ValueError:
            etiqueta_mesaje_venta.config(text="Escibe una id valida!", fg="red")

    tk.Button(ventana_venta, text="Confirmar", command=confirmar_venta).pack(pady=10)
        

def abrir_ventana_eliminar():
    # 1. Creamos la ventana secundaria
    ventana_eliminar = tk.Toplevel(ventana)
    ventana_eliminar.title("Eliminar Producto")
    ventana_eliminar.geometry("300x150")

    # --- ZONA DE WIDGETS DE LA VENTANA SECUNDARIA ---
    tk.Label(ventana_eliminar, text="ID del producto a eliminar", font=("Arial", 14, "bold")).pack(pady=10)

    caja_id_eliminar = tk.Entry(ventana_eliminar)
    caja_id_eliminar.pack()


    etiqueta_mensaje_eliminar = tk.Label(ventana_eliminar, text="")
    etiqueta_mensaje_eliminar.pack()



    def confirmar_eliminar():
        try:
            id_borrar = int(caja_id_eliminar.get())
            producto_a_eliminar = mi_inventario.buscar_producto_por_id(id_borrar)
            
            if not producto_a_eliminar:
                etiqueta_mensaje_eliminar.config(text=f"{id_borrar} no encontrado!", fg='red')
            else:
                producto = producto_a_eliminar[0]
                nombre_prod = producto[1]
                etiqueta_mensaje_eliminar.config(text=f"ID {id_borrar} {nombre_prod} eliminado", fg='green')
                mi_inventario.eliminar_producto(id_borrar)
                mostrar_datos()
        except ValueError:
            etiqueta_mensaje_eliminar.config(text="Escribe una ID valida", fg="red")

    tk.Button(ventana_eliminar, text="Confirmar", command=confirmar_eliminar).pack(pad=10)


# 1. creacion inventario tabla
mi_inventario = Inventario("inventario.db")
mi_inventario.crear_tabla()


# 2. Configuramos la ventana
ventana = tk.Tk()
ventana.title("Sistema Inventario")
ventana.geometry("400x500")

# ---------------------------------------ZONA DE WIDGETS ---------------------------------
titulo_venta = tk.Label(ventana, text="Agregar nuevo producto", font=("Arial", 14, "bold"))
titulo_venta.pack(pady=10)

# NOMBRE
etiqueta_guardar_nombre =  tk.Label(ventana, text="Nombre")
etiqueta_guardar_nombre.pack()
caja_guardar_nombre = tk.Entry(ventana)
caja_guardar_nombre.pack()

# CANTIDAD
etiqueta_guardar_cantidad = tk.Label(ventana, text="Cantidad") 
etiqueta_guardar_cantidad.pack()
caja_guardar_cantidad = tk.Entry(ventana)
caja_guardar_cantidad.pack()

# PRECIO
etiqueta_guardar_precio =  tk.Label(ventana, text="Precio")
etiqueta_guardar_precio.pack()
caja_guardar_precio = tk.Entry(ventana)
caja_guardar_precio.pack()
  
# BOTON
boton_guardar = tk.Button(ventana, text="Guardar producto", command=guardar_datos)
boton_guardar.pack()

# CONFIRMACION LABEL
etiqueta_confirmacion = tk.Label(ventana, text="")
etiqueta_confirmacion.pack()

# ------------------------------------ ZONA DE LECTURA DE INVENTARIO ------------------------------------------------
separador = tk.Label(ventana, text="---Inventario Actual ---", font=("Arial", 12, "bold"))
separador.pack(pady=10)

boton_mostrar = tk.Button(ventana, text="Mostrar productos", command=mostrar_datos)
boton_mostrar.pack(pady=10)

boton_eliminar = tk.Button(ventana, text="Abrir ventana Eliminar", command=abrir_ventana_eliminar)
boton_eliminar.pack(pady=10)

boton_vender = tk.Button(ventana, text="Abrir ventana ventas", command=abrir_ventana_venta)
boton_vender.pack(pady=10)

# --- NUEVA TABLA PARA VISUALIZAR LOS PRODUCTOS (Treeview) ---
# 1. Definimos los nombres internos de las columnas
columnas = ("ID", "NOMBRE", "PRECIO", "CANTIDAD")
tabla_productos = ttk.Treeview(ventana, columns=columnas, show="headings", height=8)

# 2. Configuramos el texto que se verá en el encabezado de cada columna
tabla_productos.heading("ID", text="ID")
tabla_productos.heading("NOMBRE", text="NOMBRE")
tabla_productos.heading("CANTIDAD", text="CANTIDAD")
tabla_productos.heading("PRECIO", text="PRECIO")

# 3. Configuramos el ancho de las columnas (en píxeles) para que se vea ordenado
tabla_productos.column("ID", width=20)
tabla_productos.column("NOMBRE", width=150)
tabla_productos.column("CANTIDAD", width=70)
tabla_productos.column("PRECIO", width=70)

tabla_productos.pack()


ventana.mainloop()