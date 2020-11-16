from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name="carrito"

urlpatterns = [
    path('agregar_producto/<int:producto_id>', login_required(agregar_producto, login_url='/accounts/login') , name="agregar_producto"),
    path('eliminar_producto/<int:producto_id>', eliminar_producto, name="eliminar_producto"),
    path('disminuir_producto/<int:producto_id>', disminuir_producto, name="disminuir_producto"),
    path('Limpiar/', limpiar_carrito, name="limpiar_carrito"),




]