# quando começar
# git pull origin main

# Quando terminar o expediente
# github git add .
# git commit -m "Resumo do que foi feito no serviço hoje"
# git push origin main

class Produtos:
    lista_productos = []

    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

        Produtos.lista_productos.append(self)

    def __repr__(self):
        return f"""
ID: {self.id}
NOMBRE: {self.nombre}
PRECIO: {self.precio}
CANTIDAD: {self.cantidad}
{"="*50}
"""
    @classmethod
    def guardad_producto(cls, id, nombre, precio,cantidad):
        novo = cls(id, nombre, precio, cantidad)
        return novo

a1 = Produtos.guardad_producto(1, "vasoura", 10, 50)
a2 = Produtos.guardad_producto(2, "espude", 5, 50)
print(Produtos.lista_productos)

