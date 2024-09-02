from controllers.Controller_product import Controller_product

class Product_view:
    def __init__(self):
        self.controlador = Controller_product()
    
    def mostrar_menu(self):
        while True:
            self._mostrar_opciones()
            opcion = self._leer_opcion()
            
            if opcion == '1':
                self.agregar_producto()
            elif opcion == '2':
                print("Saliendo...")
                break
            else:
                self._mostrar_error("Opción no válida, por favor elige nuevamente.")
    
    def _mostrar_opciones(self):
        print("\n--- Sistema de Venta de Productos ---")
        print("1. Agregar Producto")
        print("2. Salir")

    def _leer_opcion(self):
        return input("Elige una opción: ")

    def _mostrar_error(self, mensaje):
        print(f"Error: {mensaje}")

    def agregar_producto(self):
        while True:
            try:
                no_articulo = self._leer_numero("Ingrese el No Artículo (999 para salir): ")
                
                # Condición para salir del bucle
                if no_articulo == 999:
                    print("Regresando al menú principal...")
                    break
                
                descripcion = input("Ingrese la Descripción: ")
                precio_compra = self._leer_numero("Ingrese el Precio de Compra: ", es_float=True)
                existencia = self._leer_numero("Ingrese la Existencia: ")
                
                producto = self.controlador.crear_producto(no_articulo, descripcion, precio_compra, existencia)
                print(f"Producto '{producto.descripcion}' agregado con éxito!")
            
            except ValueError as e:
                self._mostrar_error(str(e))
    
    def _leer_numero(self, mensaje, es_float=False):
        while True:
            try:
                valor = input(mensaje)
                if es_float:
                    return float(valor)
                else:
                    return int(valor)
            except ValueError:
                self._mostrar_error("Valor inválido, por favor ingrese un número.")
