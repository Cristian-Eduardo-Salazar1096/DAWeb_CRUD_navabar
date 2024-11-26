from django.shortcuts import render,redirect,get_object_or_404
from .models import Pedidos
# Create your views here.

def inicio_vistaPedido(request):
    losPedidos=Pedidos.objects.all()
    return render(request,"gestionarPedidos.html",{"misPedidos":losPedidos})

def registrarPedido(request):
    id_pedido=request.POST["id_pedido"]
    nombre=request.POST["nombre"]
    fech=request.POST["fech"]
    id_Cliente=request.POST["id_Cliente"]
    Costo=request.POST["Costo"]
    Direccion=request.POST["Direccion"]
    Cantidad=request.POST["Cantidad"]
    guardarpedido=Pedidos.objects.create(id_pedido=id_pedido,nombre=nombre,fech=fech,id_Cliente=id_Cliente,Costo=Costo,Direccion=Direccion,Cantidad=Cantidad)
    return redirect("pedido")

def seleccionarPedido(request, id_pedido):
    pedido = get_object_or_404(Pedidos, id_pedido=id_pedido)
    return render(request, "editarPedidos.html", {"pedido": pedido})

def editarPedido(request, id_pedido):
    pedido = get_object_or_404(Pedidos, id_pedido=id_pedido)

    if request.method == "POST":
        pedido.nombre = request.POST.get("nombre")
        pedido.fech = request.POST.get("fech")
        pedido.id_Cliente = request.POST.get("id_Cliente")
        pedido.Costo = request.POST.get("Costo")
        pedido.Direccion = request.POST.get("Direccion")
        pedido.Cantidad = request.POST.get("Cantidad")
        pedido.save()
        return redirect("pedido") 
    
    return render(request, "editarPedidos.html", {"pedido": pedido})



def borrarPedido(request, id_pedido):
    pedido = Pedidos.objects.get(id_pedido=id_pedido)
    pedido.delete()
    return redirect("pedido")