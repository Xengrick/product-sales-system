from models.Product import Product

class Controller_product:
    def __init__(self):
        self.productos = []

    def crear_producto(self, no_articulo, descripcion, precio_compra, existencia):
        producto = Product(no_articulo, descripcion, precio_compra, existencia)
        self.productos.append(producto)
        return producto
