import sqlite3

class Producto:

    @classmethod
    def from_dict(cls, diccionario):
        return cls(
        diccionario['id'],
        diccionario['nombre'],
        diccionario['precio'],
        diccionario['cantidad']
        )


    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def vender(self, cantidad_a_vender):
        if self.cantidad >= cantidad_a_vender:
            self.cantidad -= cantidad_a_vender
            return self.precio *cantidad_a_vender
        return 0

    def ajustar_stock(self, tipo_ajuste, cantidad_a_ajustar):
        if tipo_ajuste == 'e':
            self.cantidad += cantidad_a_ajustar
            return True
        elif tipo_ajuste == 's':
            if self.cantidad >= cantidad_a_ajustar:
                self.cantidad -= cantidad_a_ajustar
                return True
            return False

    def to_dict(self): #serializacion
        return {'id': self.id, 'nombre': self.nombre, 'precio': self.precio, 'cantidad': self.cantidad}
 
class Inventario:
    def __init__(self):
        self.productos = []
        self.nombre_db = "inventario.db"
        self.crear_tabla()

    def ejecutar_consulta(self, instruccion_sql, datos_reales=()):
        conn = sqlite3.connect(self.nombre_db)
        cursor = conn.cursor()
        cursor.execute(instruccion_sql, datos_reales)
        conn.commit()
        resultado = cursor.fetchall() # Atrapa todo lo que el archivero encontró
        conn.close()
        return resultado

    def crear_tabla(self):
        # SQL para crear la tabla si no existe (con sus columnas estrictas)
        instruccion_sql = """
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            cantidad REAL NOT NULL,
            precio REAL NOT NULL
        )
        """
        self.ejecutar_consulta(instruccion_sql)

    def obtener_todos_los_productos(self):
        """
        retorna un diccionario con tuplas de todos los productos\n
        ex: [ (1, 'MANZANA', 100.0, 2.50), (2, 'PERA', 50.0, 3.10) ]
        """
        instruccion = "SELECT * FROM productos"
        registros = self.ejecutar_consulta(instruccion)
        return registros 

    def agregar_producto(self, nuevo_producto):
        """
        adiciona un producto en la base de datos
        """
        instruccion =  "INSERT INTO productos (nombre, precio, cantidad) VALUES (?,?,?)"
        datos_reales = (nuevo_producto.nombre, nuevo_producto.precio, nuevo_producto.cantidad)
        self.ejecutar_consulta(instruccion, datos_reales)


    def buscar_producto_por_id(self, id_buscar):
        """
        return producto entocntrado ex: [(1, 'MANZANA', 100.0, 2.50)]
        >>> [] si no existe
        """

        instruccion = "SELECT * FROM productos WHERE id = ?"
        id_real= (id_buscar,)
        producto_encontrado = self.ejecutar_consulta(instruccion, id_real)
        return producto_encontrado

    def eliminar_producto(self, id_eliminar):
        instruccion = 'DELETE FROM productos WHERE id = ?'
        id_real_eliminar = (id_eliminar,)
        self.ejecutar_consulta(instruccion, id_real_eliminar)

    def vender_producto(self, id_venda, nueva_cantidad):
        instruccion = 'UPDATE productos SET cantidad = ? WHERE id =  ?'
        valores_reales = (nueva_cantidad, id_venda)
        self.ejecutar_consulta(instruccion, valores_reales)




