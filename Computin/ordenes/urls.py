from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('procesar_orden/', procesar_orden , name="procesar_orden"),
    path('pedidos/', login_required(OrderList.as_view(), login_url='/accounts/login/') , name="mis_pedidos"),
    path('<int:pk>', login_required(OrderDetail.as_view(), login_url='/accounts/login/') , name="detalle"),

    

]