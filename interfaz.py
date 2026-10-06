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
    caja_resultados.delete("1.0", tk.END)

    registros = mi_inventario.obtener_todos_los_productos()

    if not registros:
        caja_resultados.insert(tk.END, "El inventario esta vacio!")
    else:
        for fila in registros:
            id_prod = fila[0]
            nombre = fila[1]
            cantidad = fila[2]
            precio = fila[3]

            texto_fila = f"ID: {id_prod} | NOMBRE: {nombre} |CANTIDAD: {cantidad} |PRECIO: {precio}\n"
            caja_resultados.insert(tk.END, texto_fila)


# 1. Instanciamos a nuestro Gerente y preparamos la base de datos
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
boton_mostrar.pack()

# Una caja grande (height=10 líneas de alto, width=40 letras de ancho)
caja_resultados = tk.Text(ventana, height=10, width=80)
caja_resultados.pack(pady=10)
ventana.mainloop()