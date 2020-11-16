from django.shortcuts import redirect
from producto.models import Producto
from django.contrib.auth.decorators import login_required
from .carrito import Carrito

#CRUD Carrito
@login_required(login_url="/registration/login")
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProd = producto_id)
    carrito.add(producto=producto)
    return redirect("index")

@login_required(login_url="/registration/login")
def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProd = producto_id)
    carrito.remove(producto=producto)
    return redirect("index")

@login_required(login_url="/registration/login")
def disminuir_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProd = producto_id)
    carrito.disminuir(producto=producto)
    return request("index")


@login_required(login_url="/registration/login")
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("index")