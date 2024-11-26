from django.urls import path
from Empleado_app import views
urlpatterns = [
    path('empleado', views.inicio_vistaEmpleado, name="empleado"),
    path("registrarEmpleado/",views.registrarEmpleado,name="registrarEmpleado"),
    path("seleccionarEmpleado/<int:id_empleado>",views.seleccionarEmpleado,name="seleccionarEmpleado"),
    path("editarEmpleado/<int:id_empleado>",views.editarEmpleado,name="editarEmpleado"),
    path("borrarEmpleado/<int:id_empleado>",views.borrarEmpleado,name="borrarEmpleado"),
]