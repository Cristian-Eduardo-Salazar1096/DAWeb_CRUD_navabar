from django.shortcuts import render,redirect,get_object_or_404
from .models import Provedores
# Create your views here.

def inicio_vistaProvedor(request):
    losProvedores=Provedores.objects.all()
    return render(request,"gestionarProvedores.html",{"misProvedores":losProvedores})

def registrarProvedor(request):
    id_provedor=request.POST["id_provedor"]
    nombre=request.POST["nombre"]
    Producto=request.POST["Producto"]
    Sucursal=request.POST["Sucursal"]
    HorarioE=request.POST["HorarioE"]
    HorarioS=request.POST["HorarioS"]
    Producto_Cant=request.POST["Producto_Cant"]
    Direccion=request.POST["Direccion"]
    guardarprovedor=Provedores.objects.create(id_provedor=id_provedor,nombre=nombre,Producto=Producto,Sucursal=Sucursal,HorarioE=HorarioE,HorarioS=HorarioS,Producto_Cant=Producto_Cant,Direccion=Direccion)
    return redirect("provedor")

def seleccionarProvedor(request, id_provedor):
    provedor = get_object_or_404(Provedores, id_provedor=id_provedor)
    return render(request, "editarProvedores.html", {"provedor": provedor})

def editarProvedor(request, id_provedor):
    provedor = get_object_or_404(Provedores, id_provedor=id_provedor)

    if request.method == "POST":
        provedor.nombre = request.POST.get("nombre")
        provedor.Producto = request.POST.get("Producto")
        provedor.Sucursal = request.POST.get("Sucursal")
        provedor.HorarioE = request.POST.get("HorarioE")
        provedor.HorarioS = request.POST.get("HorarioS")
        provedor.Producto_Cant = request.POST.get("Producto_Cant")
        provedor.Direccion = request.POST.get("Direccion")
        provedor.save()
        return redirect("provedor") 
    
    return render(request, "editarProvedores.html", {"provedor": provedor})



def borrarProvedor(request, id_provedor):
    provedor = Provedores.objects.get(id_provedor=id_provedor)
    provedor.delete()
    return redirect("provedor")

# "/Provedor/editarProvedor/{{ provedor.id_provedor }}"