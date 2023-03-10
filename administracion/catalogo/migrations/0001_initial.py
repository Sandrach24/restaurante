# Generated by Django 3.2.9 on 2023-02-09 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(max_length=150)),
                ('hora', models.CharField(max_length=150)),
                ('cantidad', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, verbose_name='Ingrese sus nombres')),
                ('apellidos', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono_celular', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=400)),
                ('correo_personal', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreP', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio', models.IntegerField(max_length=150)),
                ('categoria', models.CharField(choices=[('all', 'All'), ('drinks', 'Drinks'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el nombre del rol', max_length=80, verbose_name='Ingrese el nombre del rol')),
                ('descripcion', models.TextField(help_text='Descripcion del rol', verbose_name='Ingrese descripcion detallada del rol')),
            ],
            options={
                'verbose_name': 'Permisos del sistema',
                'verbose_name_plural': 'Permisos para los usuarios',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreS', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalogo.persona')),
            ],
            bases=('catalogo.persona',),
        ),
    ]
