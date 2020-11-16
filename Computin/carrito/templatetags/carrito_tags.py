from django import template

register = template.Library()

@register.filter()
def multiply(value, arg):
    return int(value) * arg

@register.filter()
def formato_moneda(value, arg):
    return f"{arg}{value}"


# para utilizar estos filtros, se debe cargar en los html como {% load carrito_tags %}  