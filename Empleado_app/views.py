from django.shortcuts import render,redirect,get_object_or_404
from .models import Empleados
# Create your views here.

def inicio_vistaEmpleado(request):
    losEmpleados=Empleados.objects.all()
    return render(request,"gestionarEmpleados.html",{"misEmpleados":losEmpleados})

def registrarEmpleado(request):
    id_empleado=request.POST["id_empleado"]
    nombre=request.POST["nombre"]
    Direccion=request.POST["Direccion"]
    Correo=request.POST["Correo"]
    HorarioE=request.POST["HorarioE"]
    HorarioS=request.POST["HorarioS"]
    Sueldo=request.POST["Sueldo"]
    Curp=request.POST["Curp"]
    guardarempleado=Empleados.objects.create(id_empleado=id_empleado,nombre=nombre,Direccion=Direccion,Correo=Correo,HorarioE=HorarioE,HorarioS=HorarioS,Sueldo=Sueldo,Curp=Curp)
    return redirect("empleado")

def seleccionarEmpleado(request, id_empleado):
    empleado = get_object_or_404(Empleados, id_empleado=id_empleado)
    return render(request, "editarEmpleados.html", {"empleado": empleado})

def editarEmpleado(request, id_empleado):
    empleado = get_object_or_404(Empleados, id_empleado=id_empleado)

    if request.method == "POST":
        empleado.nombre = request.POST.get("nombre")
        empleado.Direccion = request.POST.get("Direccion")
        empleado.Correo = request.POST.get("Correo")
        empleado.HorarioE = request.POST.get("HorarioE")
        empleado.HorarioS = request.POST.get("HorarioS")
        empleado.Sueldo = request.POST.get("Sueldo")
        empleado.Curp = request.POST.get("Curp")
        empleado.save()
        return redirect("empleado") 
    
    return render(request, "editarEmpleados.html", {"empleado": empleado})



def borrarEmpleado(request, id_empleado):
    empleado = Empleados.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("empleado")