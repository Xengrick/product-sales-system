class Product:
    def __init__(self, no_articulo, descripcion, precio_compra, existencia):
        if no_articulo == 0 or no_articulo == 999:
            raise ValueError("El Número de Artículo no puede ser 0 ni 999.")
        
        self.no_articulo = no_articulo
        self.descripcion = descripcion
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.3
        self.existencia = existencia


