# se genera una variable global para mantener el precio total en todas las templates
def precio_total_carrito(request):
    total= 0
    if request.user.is_authenticated:
        for key, value in request.session['carrito'].items():
            total = total + (int(value['precio']) * value['cantidad'])
    return {'precio_total_carrito': total}