# Generated by Django 3.1.2 on 2020-10-19 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0013_producto_categoriaesp2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='CategoriaEsp',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='CategoriaEsp2',
        ),
    ]