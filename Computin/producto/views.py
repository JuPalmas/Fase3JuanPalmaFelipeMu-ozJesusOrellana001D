from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . models import Producto
from django.views import generic
from django import forms
from carrito.carrito import Carrito
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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

def CompraEnd(request):
    return render(
        request,
        'CompraEnd.html'
    )

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
            messages.success(request,f'Cuenta creada exitosamente, Bienvenid@s a Computin | Hola   {usernames}')
            login(request, user)
            return redirect(to="index")
        data["form"] = formulario
    return render(request,'registration/registro.html',data)

def productoadmin(request):
    todoprod = Producto.objects.all()
    return render(request,'producto/producto_admin.html',context={'todoprod':todoprod})

def productosfiltrado(request,num):

        cate = Producto.objects.all()
        num1 = num
        return render(request,'producto_filtrado.html',context={'cate':cate,'num1':num1})

def buscar(request):
    busqueda = request.GET.get('buscar')
    productos = Producto.objects.filter(NombreProd__contains=busqueda)
    return render(request, 'buscar.html', {'productos': productos})

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


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username' ,'first_name','last_name',"email","password1","password2"]


class EmailChangeForm(forms.Form):
    error_messages = {
        'email_mismatch': "Error al confirmar el email, intente nuevamente",
        'not_changed': "¡El correo ingresado es igual al anterior, no se aplicaron cambios!",
    }

    new_email1 = forms.EmailField(
        label="Ingrese su nuevo correo",
        widget=forms.EmailInput,
    )

    new_email2 = forms.EmailField(
        label="Confirme su nuevo correo",
        widget=forms.EmailInput,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EmailChangeForm, self).__init__(*args, **kwargs)

    def clean_new_email1(self):
        old_email = self.user.email
        new_email1 = self.cleaned_data.get('new_email1')
        if new_email1 and old_email:
            if new_email1 == old_email:
                raise forms.ValidationError(
                    self.error_messages['not_changed'],
                    code='not_changed',
                )
        return new_email1

    def clean_new_email2(self):
        new_email1 = self.cleaned_data.get('new_email1')
        new_email2 = self.cleaned_data.get('new_email2')
        if new_email1 and new_email2:
            if new_email1 != new_email2:
                raise forms.ValidationError(
                    self.error_messages['email_mismatch'],
                    code='email_mismatch',
                )
        return new_email2

    def save(self, commit=True):
        email = self.cleaned_data["new_email1"]
        self.user.email = email
        if commit:
            self.user.save()
        return self.user



def email_change(request):
    form = EmailChangeForm()
    if request.method=='POST':
        form = Email_Change_Form(User,request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                if form.cleaned_data['email1']  == form.cleaned_data['email2']:
                    user = request.user
                    u = User.objects.get(username=user)
                    # get the proper user
                    u.email = form.cleaned_data['email1']
                    u.save()
                    return HttpResponseRedirect("/accounts/login/")
    else:
        return render_to_response("email_change.html", {'form':form},
                                   context_instance=RequestContext(request))

