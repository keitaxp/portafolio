from django.contrib import admin
from django.forms import models
#from .models import Cliente, Cocina, Bodega, EstadoPedido, Mesas, Pedido, PedidoProducto, PedidosProductoIntermedio, ProductoReceta, Productos, Proveedor, Receta, RecetaPedido, Usuarios
from .models.models import Cliente, Cocina, Bodega, EstadoPedido, Mesa, Pedido, PedidoProducto, PedidosProductoIntermedio, ProductoReceta, Productos, Proveedor, Receta, RecetaPedido, Usuarios

admin.site.register(Cliente)
admin.site.register(Cocina)
admin.site.register(Bodega)
admin.site.register(EstadoPedido)
admin.site.register(Mesa)
admin.site.register(Pedido)
admin.site.register(PedidoProducto)
admin.site.register(PedidosProductoIntermedio)
admin.site.register(ProductoReceta)
admin.site.register(Productos)
admin.site.register(Proveedor)
admin.site.register(Receta)
admin.site.register(RecetaPedido)
admin.site.register(Usuarios)