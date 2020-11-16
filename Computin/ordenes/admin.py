from django.contrib import admin
from .models import OrderLine, Orden

admin.site.register([Orden,OrderLine])

