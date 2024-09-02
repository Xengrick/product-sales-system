import unittest
from models.Product import Product
from controllers.Controller_product import Controller_product

class ProductTest(unittest.TestCase):
    
    def setUp(self):
        self.controlador = Controller_product()

    def test_no_articulo_invalido(self):
        with self.assertRaises(ValueError):
            self.controlador.crear_producto(0, "Producto A", 10.0, 5)

        with self.assertRaises(ValueError):
            self.controlador.crear_producto(999, "Producto B", 15.0, 10)