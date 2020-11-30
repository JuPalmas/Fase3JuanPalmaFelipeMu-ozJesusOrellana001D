from django.test import TestCase
from django.urls import reverse
from producto.models import Producto


class TestViews(TestCase):
    def test_view_uses_correct_template_productos(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'producto/producto_list.html')

    def test_view_uses_correct_template_nosotros(self):
        response = self.client.get(reverse('nosotros'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nosotros.html')

    def test_view_uses_correct_template_index(self):
            response = self.client.get(reverse('index'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'index.html')
