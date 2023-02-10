from django.contrib import admin

from .models import Rol,Servicio,Producto,Cliente,Pedido




admin.site.index_title = "Bienvenidos al portal de Administración. "
admin.site.register(Servicio)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Rol)
admin.site.register(Cliente)
