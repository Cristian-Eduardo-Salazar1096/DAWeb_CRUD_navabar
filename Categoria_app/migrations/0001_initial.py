# Generated by Django 5.1.3 on 2024-11-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categoria', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('Cant_Prod', models.IntegerField(max_length=30)),
                ('Descripcion', models.CharField(max_length=100)),
                ('id_producto', models.SmallIntegerField()),
                ('Fecha_Creacion', models.DateField()),
                ('Ventas', models.IntegerField(max_length=30)),
            ],
        ),
    ]