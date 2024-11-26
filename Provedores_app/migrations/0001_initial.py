# Generated by Django 5.1.3 on 2024-11-20 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provedores',
            fields=[
                ('id_provedor', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('Producto', models.CharField(max_length=20)),
                ('Sucursal', models.CharField(max_length=50)),
                ('HorarioE', models.TimeField()),
                ('HorarioS', models.TimeField()),
                ('Producto_Cant', models.CharField(max_length=20)),
                ('Direccion', models.CharField(max_length=40)),
            ],
        ),
    ]