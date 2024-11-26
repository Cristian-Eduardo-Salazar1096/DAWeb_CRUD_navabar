from django.urls import path
from Producto_app import views
urlpatterns = [
    path('producto', views.inicio_vistaProducto, name="producto"),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<int:id_producto>",views.seleccionarProducto,name="seleccionarProducto"),
    path("editarProducto/<int:id_producto>",views.editarProducto,name="editarProducto"),
    path("borrarProducto/<int:id_producto>",views.borrarProducto,name="borrarProducto"),
]