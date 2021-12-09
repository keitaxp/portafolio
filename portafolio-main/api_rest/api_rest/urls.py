"""api_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api_rest.controler.recetacontroler import receta, recetabyid
from api_rest.controler.productocontroler import producto, productobyid
from api_rest.controler.clientecontroler import cliente, clientebyid
from api_rest.controler.rolcontroler import rol, rolbyid
from api_rest.controler.usuarioscontroler import usuarios, usuariosbyid
from api_rest.controler.pedidocontroler import pedido, pedidobyid
from api_rest.controler.bodegacontroler import bodega, bodegabyid
from api_rest.controler.proveedorcontroler import proveedor, proveedorbyid
from api_rest.controler.PedidosProductoIntermediocontroler import PedidosProductoIntermedio, PedidosProductoIntermediobyid
from api_rest.controler.mesacontroler import mesa, mesabyid
from api_rest.controler.mesa_estadocontroler import mesa_estado, mesa_estadobyid
from api_rest.controler.reservacontroler import reserva, reservabyid
from api_rest.controler.finanzascontroler import finanzas, finanzasbyid
from api_rest.controler.reservadocontroler import reservado, reservadobyid
from api_rest.controler.receta_pedidocontroler import receta_pedido, receta_pedidobyid
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/receta/', receta ),
    path('api/v1/receta/<int:id>', recetabyid ),
    path('api/v1/producto/', producto ),
    path('api/v1/producto/<int:id>',productobyid),
    path('api/v1/cliente/', cliente ),
    path('api/v1/cliente/<int:id>', clientebyid ),
    path('api/v1/rol/', rol ),
    path('api/v1/rol/<int:id>',rolbyid ),
    path('api/v1/usuarios/', usuarios ),
    path('api/v1/usuarios/<int:id>',usuariosbyid ),
    path('api/v1/pedido/', pedido ),
    path('api/v1/pedido/<int:id>',pedidobyid),
    path('api/v1/bodega/', bodega ),
    path('api/v1/bodega/<int:id>',bodegabyid),
    path('api/v1/proveedor/', proveedor ),
    path('api/v1/proveedor/<int:id>',proveedorbyid),
    path('api/v1/PedidosProductoIntermedio/', PedidosProductoIntermedio ),
    path('api/v1/PedidosProductoIntermedio/<int:id>',PedidosProductoIntermediobyid),
    path('api/v1/mesa/', mesa ),
    path('api/v1/mesa/<int:id>',mesabyid),
    path('api/v1/mesa_estado/', mesa_estado ),
    path('api/v1/mesa_estado/<int:id>',mesa_estadobyid),
    path('api/v1/reserva/', reserva ),
    path('api/v1/reserva/<int:id>',reservabyid),
    path('api/v1/finanzas/', finanzas ),
    path('api/v1/finanzas/<int:id>',finanzasbyid),
    path('api/v1/reservado/', reservado ),
    path('api/v1/reservado/<int:id>',reservadobyid),
    path('api/v1/receta_pedido/', receta_pedido ),
    path('api/v1/receta_pedido/<int:id>',receta_pedidobyid),
    

    

    
]
