from django import forms

from . models import Producto

class ProductoForms(forms.ModelForm):

    idProd = forms.CharField(label='id',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    NombreProd = forms.CharField(label='Nombre Producto',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    MarcaProd = forms.CharField(label='Marca',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    CategoriaProd = forms.CharField(label='Categoria Producto',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    CategoriaEsp = forms.CharField(label='Categoria Especial',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    PrecioProd = forms.CharField(label='Precio',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    StockProd = forms.CharField(label='Precio',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    DescripcionProd = forms.CharField(label='descripción',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Producto
        fields = ('idProd','NombreProd', 'MarcaProd', 'CategoriaProd','CategoriaEsp','PrecioProd','StockProd','DescripcionProd')