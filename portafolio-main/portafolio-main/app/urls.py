# direcciones de nuetra aplicacion

from django.urls import path
from .views import home, proveedor_view, productoView, registro, adminReceta, base2, adminUsuario, adminProductoview, adminRecetaView , adminProveedorview
#from ..api_rest.api_rest.business.recetabusiness import 



urlpatterns = [
    path('', home, name="home"),
    path('registration/registro/',registro, name="registro"),
    path('proveedor/', proveedor_view, name= "proveedor"),
    path('producto/', productoView, name= "producto"),
    path('adminReceta/', adminRecetaView, name= "adminReceta"),  
    path('adminReceta/', adminReceta, name= "adminReceta"),
    path('base2/', base2, name= "base2"),
    path('adminUsuario/', adminUsuario, name= "adminUsuario"),
    path('adminProducto/', adminProductoview, name= "adminProducto"),
    path('adminProveedor/', adminProveedorview, name= "adminProveedor"),
    
    

    

    


    
]

