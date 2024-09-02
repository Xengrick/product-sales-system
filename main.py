from views.Product_view import Product_view

class Main:
    def __init__(self):
        self.view = Product_view()
    
    def run(self):
        self.view.mostrar_menu()

if __name__ == "__main__":
    app = Main()
    app.run()
