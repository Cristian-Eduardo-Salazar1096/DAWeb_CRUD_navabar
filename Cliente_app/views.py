from django.shortcuts import render,redirect,get_object_or_404
from .models import Clientes
# Create your views here.

def inicio_vistaCliente(request):
    losClientes=Clientes.objects.all()
    return render(request,"gestionarClientes.html",{"misClientes":losClientes})

def registrarCliente(request):
    id_cliente=request.POST["id_cliente"]
    nombre=request.POST["nombre"]
    Membresia=request.POST["Membresia"]
    Fech_Nac=request.POST["Fech_Nac"]
    Telefono=request.POST["Telefono"]
    Correo=request.POST["Correo"]
    Curp=request.POST["Curp"]
    guardarcliente=Clientes.objects.create(id_cliente=id_cliente,nombre=nombre,Membresia=Membresia,Fech_Nac=Fech_Nac,Telefono=Telefono,Correo=Correo,Curp=Curp)
    return redirect("cliente")

def seleccionarCliente(request, id_cliente):
    cliente = get_object_or_404(Clientes, id_cliente=id_cliente)
    return render(request, "editarClientes.html", {"cliente": cliente})

def editarCliente(request, id_cliente):
    cliente = get_object_or_404(Clientes, id_cliente=id_cliente)

    if request.method == "POST":
        cliente.nombre = request.POST.get("nombre")
        cliente.Membresia = request.POST.get("Membresia")
        cliente.Fech_Nac = request.POST.get("Fech_Nac")
        cliente.Telefono = request.POST.get("Telefono")
        cliente.Correo = request.POST.get("Correo")
        cliente.Curp = request.POST.get("Curp")
        cliente.save()
        return redirect("cliente") 
    
    return render(request, "editarClientes.html", {"cliente": cliente})



def borrarCliente(request, id_cliente):
    cliente = Clientes.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("cliente")

# "/Empleado/editarEmpleado/{{ empleado.id_empleado }}"