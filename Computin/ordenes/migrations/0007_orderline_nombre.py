# Generated by Django 3.1.3 on 2020-11-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0006_orden_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
