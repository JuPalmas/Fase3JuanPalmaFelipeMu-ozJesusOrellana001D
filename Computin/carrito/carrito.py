# se crea el carrito, utilizando la sesión actual y agregando productos a la lista
class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito


    # Comprobar si existen productos y agregar productos // revisar luego si el es producto.id o producto.idprod //
    def add(self, producto):
        if str(producto.idProd) not in self.carrito.keys():
            self.carrito[producto.idProd] = {
                "producto_id": producto.idProd,
                "nombre": producto.NombreProd,
                "cantidad": 1,
                "precio": str(producto.PrecioProd),
                "imagen": producto.imageProd.url
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.idProd):
                    value["cantidad"] = value["cantidad"] + 1                    
                    break
        self.save()


    # Guardar el carrito en la sesión
    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True


    # Eliminar un producto del carrito
    def remove(self,producto):
        producto_id = str(producto.idProd)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.save()

    # Disminuir cantidad en el carrito
    def disminuir(self, producto):
        for key, value in self.carrito.items():
                if key == str(producto.idProd):
                    value["cantidad"] = value["cantidad"] - 1   
                    if value["cantidad"]<1:
                        self.remove(producto)
                    else:
                        self.save()
                    break
                else:
                    print("El producto no existe en el carrito")
        
    # Limpiar     
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True