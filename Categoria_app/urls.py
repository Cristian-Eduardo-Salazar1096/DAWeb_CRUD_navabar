from django.urls import path
from Categoria_app import views
urlpatterns = [
    path('categoria', views.inicio_vistaCategoria, name="categoria"),
    path("registrarCategoria/",views.registrarCategoria,name="registrarCategoria"),
    path("seleccionarCategoria/<int:id_categoria>",views.seleccionarCategoria,name="seleccionarCategoria"),
    path("editarCategoria/<int:id_categoria>",views.editarCategoria,name="editarCategoria"),
    path("borrarCategoria/<int:id_categoria>",views.borrarCategoria,name="borrarCategoria"),
]