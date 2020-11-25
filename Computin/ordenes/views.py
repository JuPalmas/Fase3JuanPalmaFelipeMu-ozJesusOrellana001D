from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Orden, OrderLine
from carrito.carrito import Carrito


@login_required(login_url='/accounts/login')
def procesar_orden(request):
    orden = Orden.objects.create(user=request.user, completado=True)
    carrito = Carrito(request)
    order_lines = list()
    for key, value in carrito.carrito.items():
        order_lines.append(
            OrderLine(
                producto_id=key,
                cantidad=value["cantidad"],
                user=request.user,
                orden=orden
            )
        )

    # bulk_create : crea registros en la bdd usando los datos del for
    OrderLine.objects.bulk_create(order_lines)

    # enviar email al cliente
    enviar_email_orden(
        orden=orden,
        order_lines=order_lines,
        username=request.user.username,
        email=request.user.email
    )

    carrito.limpiar()

    messages.success(request, "El pedido se ha creado correctamente!")
    return redirect("CompraEnd")

# Configurando el correo de la orden
def enviar_email_orden(**kwargs):
    subject = "Gracias por tu pedido"
    html_message = render_to_string("emails/nuevo_pedido.html", {
        "orden": kwargs.get("orden"),
        "order_lines": kwargs.get("order_lines"),
        "username": kwargs.get("username")
    })
    plain_message = strip_tags(html_message)
    from_email = "admin@computin.cl"
    to = kwargs.get("email")
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

#Mostrar lista de pedidios del usuario
class OrderList(ListView):
    model = Orden
    ordering = ["-id"]
    template_name = "ordenes/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

#Muestra el detalle de un pedido
class OrderDetail(DetailView):
    model = Orden
    template_name = "ordenes/detalle.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
