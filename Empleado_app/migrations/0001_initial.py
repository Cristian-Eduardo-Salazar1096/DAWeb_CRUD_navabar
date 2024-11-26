# Generated by Django 5.1 on 2024-11-19 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id_empleado', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=100)),
                ('Correo', models.CharField(max_length=100)),
                ('HorarioE', models.TimeField()),
                ('HorarioS', models.TimeField()),
                ('Sueldo', models.IntegerField(max_length=50)),
                ('Curp', models.CharField(max_length=100)),
            ],
        ),
    ]
