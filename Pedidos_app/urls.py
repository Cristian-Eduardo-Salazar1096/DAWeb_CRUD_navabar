from django.urls import path
from Pedidos_app import views
urlpatterns = [
    path('pedido', views.inicio_vistaPedido, name="pedido"),
    path("registrarPedido/",views.registrarPedido,name="registrarPedido"),
    path("seleccionarPedido/<int:id_pedido>",views.seleccionarPedido,name="seleccionarPedido"),
    path("editarPedido/<int:id_pedido>",views.editarPedido,name="editarPedido"),
    path("borrarPedido/<int:id_pedido>",views.borrarPedido,name="borrarPedido"),
]