from django.shortcuts import render,redirect,get_object_or_404
from .models import Categorias
# Create your views here.

def inicio_vistaCategoria(request):
    lasCategorias=Categorias.objects.all()
    return render(request,"gestionarCategorias.html",{"misCategorias":lasCategorias})

def registrarCategoria(request):
    id_categoria=request.POST["id_categoria"]
    nombre=request.POST["nombre"]
    Cant_Prod=request.POST["Cant_Prod"]
    Descripcion=request.POST["Descripcion"]
    id_producto=request.POST["id_producto"]
    Fecha_Creacion=request.POST["Fecha_Creacion"]
    Ventas=request.POST["Ventas"]
    guardarcategoria=Categorias.objects.create(id_categoria=id_categoria,nombre=nombre,Cant_Prod=Cant_Prod,Descripcion=Descripcion,id_producto=id_producto,Fecha_Creacion=Fecha_Creacion,Ventas=Ventas)
    return redirect("/Categoria")

def seleccionarCategoria(request, id_categoria):
    categoria = get_object_or_404(Categorias, id_categoria=id_categoria)
    return render(request, "editarCategorias.html", {"categoria": categoria})

def editarCategoria(request, id_categoria):
    categoria = get_object_or_404(Categorias, id_categoria=id_categoria)

    if request.method == "POST":
        categoria.nombre = request.POST.get("nombre")
        categoria.Cant_Prod = request.POST.get("Cant_Prod")
        categoria.Descripcion = request.POST.get("Descripcion")
        categoria.id_producto = request.POST.get("id_producto")
        categoria.Fecha_Creacion = request.POST.get("Fecha_Creacion")
        categoria.Ventas = request.POST.get("Ventas")
        categoria.save()
        return redirect("/Categoria") 
    
    return render(request, "editarCategorias.html", {"categoria": categoria})



def borrarCategoria(request, id_categoria):
    categoria = Categorias.objects.get(id_categoria=id_categoria)
    categoria.delete()
    return redirect("/Categoria")

# "/Provedor/editarProvedor/{{ provedor.id_provedor }}"