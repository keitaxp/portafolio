from django import forms
from django.db.models import fields
from .models.models import Productos, Proveedor, Receta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            
            'nombre_proveedor',
            'apellido_proveedor',
            'rut_proveedor',
            'contacto', 

        ]
       
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [

            'id_proveedor',
            'nombre_producto',
            'descripcion',
        
        
        
        
        ]


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [ 

            'precio', 
            'nombre', 
            'descripcion',
        ]
             



class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]