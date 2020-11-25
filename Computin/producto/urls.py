from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('ofertas', views.ofertas, name='ofertas'),
    path('productofiltrado/<int:num>', views.productosfiltrado, name='productos-filtrado'),
    path('Comprado/', views.CompraEnd, name='CompraEnd'),
    path('Misdatos/ingresar', views.MisdatosCreate.as_view(), name='ingresar-datos'),
    path('productos/', views.ProductosListView.as_view(), name='productos'),
    path('producto/<int:pk>', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html') , name='login'),
    path('registro/', views.registro , name="registro"),
    path('agregarprod/', views.ProductoCreate.as_view(),name="agregarprod"),
    path('modificar/<int:pk>', views.ProcutoUpdate.as_view(),name="modificar"),
    path('producto_admin/',views.productoadmin,name='producto_admin'),
    path('eliminarprod/<int:pk>',views.ProductoDelete.as_view(),name='eliminarprod'),
    path('buscar/', views.buscar, name="buscar"),


]



