# Generated by Django 3.1.2 on 2020-10-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0008_auto_20201019_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='CategoriaEsp',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='CategoriaProd',
            field=models.CharField(max_length=150, null=True),
        ),
    ]