from django.test import TestCase
from producto.forms import ProductoForms
from producto.models import Producto


class ProductoFormsTest(TestCase):
    def test_valid_form(self):
        prod = Producto.objects.create(NombreProd = "audifonos prueba" , MarcaProd = "marca chancho")
        data = {'NombreProd': prod.NombreProd,'MarcaProd': prod.MarcaProd,}
        form = ProductoForms(data)
        self.assertTrue(form)

    def test_invalid_form(self):
        prod = Producto.objects.create(NombreProd = "" , MarcaProd= "marca chancho")
        data = {'NombreProd': prod.NombreProd,'MarcaProd': prod.MarcaProd}
        form = ProductoForms(data)
        self.assertTrue(form)


