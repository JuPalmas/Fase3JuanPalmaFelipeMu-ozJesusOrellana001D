from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . models import Producto
from . models import Compra
from django.views import generic
from django import forms
from carrito.carrito import Carrito
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    num_Productos = Producto.objects.all().count()
    num_Prod_Disp = Producto.objects.all().count()
    num_Prod = Producto.objects.all()
    DestacadoProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Destacados') #icontains sirve para buscar entre mayus y minus
    OfertaProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Ofertas')
    PopularProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Populares')
    num_visitas=request.session.get('num_visitas',0)
    num_visitas=request.session['num_visitas']=num_visitas+1
    carrito = Carrito(request)

    return render(
        request,
        'index.html',
        context={'num_Productos': num_Productos,'num_Prod_Disp': num_Prod_Disp, 'num_Prod' : num_Prod,
        'DestacadoProd' : DestacadoProd, 'OfertaProd' : OfertaProd, 'PopularProd' : PopularProd,'num_visitas':num_visitas}
    )

def nosotros(request):
    return render(request,'nosotros.html')


def ofertas(request):
    DestacadoProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Destacados') #icontains sirve para buscar entre mayus y minus
    OfertaProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Ofertas')
    PopularProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Populares')
    return render(
        request,
        'ofertas.html',
        context= {'DestacadoProd' : DestacadoProd,
        'OfertaProd' : OfertaProd, 'PopularProd' : PopularProd},
    )

def CompraEnd(request):
    return render(
        request,
        'CompraEnd.html'
    )

def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            usernames=formulario.cleaned_data["username"]
            messages.success(request,f"{usernames}")
            login(request, user)
            return redirect(to="index")
        data["form"] = formulario
    return render(request,'registration/registro.html',data)

def productoadmin(request):
    todoprod = Producto.objects.all()
    return render(request,'producto/producto_admin.html',context={'todoprod':todoprod})



from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ProductoDetailView(generic.DetailView):
    model = Producto

class ProductosListView(generic.ListView):
    model = Producto

class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'

class ProcutoUpdate(UpdateView):
    model = Producto
    fields = '__all__'

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('index')

class CompraCreate(CreateView):
    model = Compra
    fields = '__all__'

class CompraDetailView(generic.DetailView):
    model = Compra

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username' ,'first_name','last_name',"email","password1","password2"]

