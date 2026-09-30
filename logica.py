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

    def agregar_producto(self, nuevo_producto):
        """
        adiciona un producto a la lista self.productos
        """
        self.productos.append(nuevo_producto)

    def buscar_producto_por_id(self, id_buscar):
        """
        itera la lista de clase inventario para identificar el id_buscar\n
        si hay match de id devuelve el diccionario del prodcuto
        >>> None si no hay match de id
        """
        for producto in self.productos:
            if producto.id == id_buscar:
                return producto
        return None

    def eliminar_producto_por_id(self,id_eliminar):
        """
        >>> True si elimina el producto del diccionario si lo encuentra con match del id de funcion buscar producto por id
        >>> False si no hay math al usar funcion buscar prodcuto por id
        """
        busca_producto = self.buscar_producto_por_id(id_eliminar)
        if busca_producto is None:
            return False
        self.productos.remove(busca_producto)
        return True

    def siguiente_id(self):
        """
        retorna el numero de id mas alto de toda la lista + 1
        >>> None si la lista esta vacia
        """
        if not self.productos:
            return 1
        id_maximo = max(p.id for p in self.productos) + 1
        return id_maximo