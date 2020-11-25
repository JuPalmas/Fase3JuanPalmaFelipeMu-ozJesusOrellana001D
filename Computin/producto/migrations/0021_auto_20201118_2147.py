# Generated by Django 3.1.3 on 2020-11-19 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producto', '0020_auto_20201027_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Misdatos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('correo', models.CharField(max_length=150)),
                ('numTelefonico', models.IntegerField(max_length=15, null=True)),
                ('comuna', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('comentario', models.CharField(blank=True, max_length=150, null=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
    ]