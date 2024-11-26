from django.shortcuts import render,redirect,get_object_or_404
from .models import Productos
# Create your views here.

def inicio_vistaProducto(request):
    losProductos=Productos.objects.all()
    return render(request,"gestionarProductos.html",{"misProductos":losProductos})

def registrarProducto(request):
    id_producto=request.POST["id_producto"]
    nombre=request.POST["nombre"]
    precio=request.POST["precio"]
    Cantidad=request.POST["Cantidad"]
    Descripcion=request.POST["Descripcion"]
    Categoria=request.POST["Categoria"]
    Fech_Cad=request.POST["Fech_Cad"]
    guardarproducto=Productos.objects.create(id_producto=id_producto,nombre=nombre,precio=precio,Cantidad=Cantidad,Descripcion=Descripcion,Categoria=Categoria,Fech_Cad=Fech_Cad)
    return redirect("producto")

def seleccionarProducto(request,id_producto):
    producto=get_object_or_404(Productos, id_producto=id_producto)
    return render(request,"editarProductos.html",{"producto":producto})

def editarProducto(request,id_producto):
    producto=get_object_or_404(Productos, id_producto=id_producto)
    
    if request.method == "POST":
        producto.nombre=request.POST.get("nombre")
        producto.precio=request.POST.get("precio")
        producto.Cantidad=request.POST.get("Cantidad")
        producto.Descripcion=request.POST.get("Descripcion")
        producto.Categoria=request.POST.get("Categoria")
        producto.Fech_Cad=request.POST.get("Fech_Cad")
        producto.save()
        return redirect("producto")
    
    return render(request, "editarProductos.html", {"producto":producto})


def borrarProducto(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("producto")