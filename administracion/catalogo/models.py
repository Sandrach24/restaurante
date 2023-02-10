from django.db import models

# Create your models here.

from email.policy import default
from pickle import FALSE
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.db.models.deletion import CASCADE
from datetime import datetime

# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(verbose_name='Ingrese el nombre del rol', max_length=80, help_text='Ingrese el nombre del rol')
    descripcion = models.TextField(verbose_name='Ingrese descripcion detallada del rol', help_text='Descripcion del rol')

    class Meta:
        verbose_name = 'Permisos del sistema'
        verbose_name_plural = 'Permisos para los usuarios'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    #renombrar el metodo guardar de la clase rol
    #dentro del metodo consideramos self(clase rol)
    #*args -> captura todos los elementos de django y de la clase rol
    #**Kwards -> captura todos los elementos de django y de la clase rol y adiciona los argumentos de la interfaz web
    def save(self, *args, **Kwargs):
        # dar la posibilidad de seleccionar que permisos se pueden dar
        permisos_defecto = ['add','change','delete','view']
        #verificar si el rol que estamos creando no ha sido ingresado anteriormente
        if not self.id:
            nuevo_grupo, creado = Group.objects.get_or_create(name=f'{self.nombre}')
            for permiso_temp in permisos_defecto:
                permiso, created = Permission.objects.update_or_create(
                    name = f'Can {permiso_temp} {self.nombre}',
                    content_type = ContentType.objects.get_for_model(Rol),
                    codename = f'{permiso_temp}_{self.nombre}'
                )
                if creado:
                    nuevo_grupo.permissions.add(permiso.id)
            super().save(*args, **Kwargs)
        else:
            rol_antiguo = Rol.objects.filter(id=self.id).values('nombre').first
            if rol_antiguo['nombre'] == self.nombre:
                super().save(*args, *Kwargs)
            else:
                Group.objects.filter(name=rol_antiguo['nombre'].update(name=f'{self.nombre}'))
                for permiso_temp in permisos_defecto:
                    Permission.objects.filter(codename=f"{permiso_temp}_{rol_antiguo['nombre']}").update(
                        codename = f'{permiso_temp}_{self.nombre}',
                        name = f'Can {permiso_temp} {self.nombre}'
                    )
                super().save(*args, **Kwargs)    

class Persona(models.Model):
    nombres = models.CharField(max_length=100, verbose_name='Ingrese sus nombres')
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10)
    telefono_celular = models.CharField(max_length=10)
    direccion = models.CharField(max_length=400)
    correo_personal = models.CharField(max_length=150)
   

    def __str__(self):
        return self.cedula + " " + self.apellidos



class Producto(models.Model):

    nombreP = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField (max_length=150)
    categoria_CHOICES =[
        ('all', 'All'),
        ('drinks', 'Drinks'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    categoria = models.CharField(max_length=100, choices=categoria_CHOICES)

    def __str__(self):
        return self.nombreP

class Servicio(models.Model):
   
    nombreS= models.CharField(max_length=300)
    descripcion= models.CharField(max_length=50)  
   
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
    

    def __str__(self):
        return self.nombreS
def buscar_producto():
    producto =  Producto.objects.all().filter(codigo_pedido = "E00001")
    print("Su pedido es:" , producto)
    return producto

class Pedido(models.Model):
    fecha = models.DateField(max_length=150)
    hora = models.CharField(max_length=150)
    cantidad = models.CharField(max_length=150)
    estado_CHOICES =[
        ('en espera', 'EN ESPERA'),
        ('en preparacion', 'EN PREPARACION '),
        ('entregado', 'ENTREGADO'),
    ]

class Cliente (Persona):
    ESTADO_CHOICES =[
        ('docente', 'DOCENTE'),
        ('estudiante', 'ESTUDIANTE'),
       
    ]

    


   

 