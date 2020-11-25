from django.db import models
from django.urls import reverse # Se utiliza para direccionar los path de nmuestro proyecto asociado al modelo
import uuid # Se utiliza para relacionar objetos de de Instancia de productos
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Producto(models.Model):
	idProd = models.IntegerField(primary_key=True,help_text='Id única del producto')
	NombreProd = models.CharField(max_length=150)
	MarcaProd = models.CharField(max_length=150)
	CategoriaProd = models.CharField(max_length=150,null=True)
	CategoriaEsp = models.CharField(max_length=150,null=True,help_text='Categorias especiales (Destacados,Ofertas,Populares).Sino posee dejar como "Ninguno"')
	PrecioProd = models.IntegerField(null=True)
	StockProd = models.IntegerField(null=True)
	imageProd = models.ImageField(upload_to='imagesProd/', null=True, blank=True)
	DescripciónProd = models.TextField(max_length=5000)

	def __str__(self):
		return self.NombreProd

	def get_absolute_url(self):
		return reverse('producto-detail', args=[int(self.idProd)])

class Misdatos(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    correo= models.CharField(max_length=150)
    numTelefonico = models.IntegerField(max_length=15 , null=True)
    regiones = (
        ('I', 'Arica y Parinacota y Tarapacá'),
        ('II', 'Antofagasta'),
        ('III', 'Atacama y Coquimbo'),
        ('IV', 'Valparaíso'),
        ('V', 'O Higgins'),
        ('VI', 'Maule'),
        ('VII', 'Ñuble, Biobío y La Araucanía (norte)'),
        ('VIII', 'La Araucanía (sur)'),
        ('IX', 'Los Ríos y Los Lagos(norte)'),
        ('X', '    Los Lagos(Sur) y Aysén'),
        ('XI', 'Magallanes'),
        ('RM', 'Metropolitana de Santiago'),
    )
    region = models.CharField(
        max_length=4,
        choices=regiones,
        blank=True,
        default='RM',
        help_text='Seleccione una región',
    )
    comuna = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    comentario = models.CharField(max_length=150,null=True, blank=True)


    def str(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('login')