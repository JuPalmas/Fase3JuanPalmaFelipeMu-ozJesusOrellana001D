# Generated by Django 3.1.2 on 2020-10-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_producto_imageprod'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='CategoriaEsp',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='CategoriaProd',
            field=models.IntegerField(null=True),
        ),
    ]
