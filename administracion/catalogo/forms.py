from django import forms
from .models import Pedido, Cliente, Producto


class PedidoForms(forms.ModelForm):
    
    class Meta:
        model = Pedido
        fields = ('fecha','hora','cantidad','estado')

class PersonForms(forms.ModelForm):
    class Meta: 
        model = Cliente
        fields=('nombres','apellidos','cedula', 'correo_personal','telefono_celular','direccion')


class ProductoForm(forms.ModelForm):
    class Meta: 
        model = Producto
        fields=('nombreP', 'descripcion','precio','categoria')
