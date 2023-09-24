from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def inicio(request):
    return render(request,'paginas_base/inicio.html')


def lista(request):
    clientes =Cliente.objects.all()
    return render(request,"Crud/listado.html",{"clientes":clientes})


        
def crear_editar(request, id=0):
    if request.method== 'GET':
        if id ==0:
            formulario=ClienteForm()
        else:
            clienteid=Cliente.objects.get(pk=id)
            formulario=ClienteForm(instance=clienteid)
        return render (request, 'Crud/crear.html',{'formulario': formulario})
    else:
        if id==0:
            formulario=ClienteForm(request.POST or None, request.FILES or None)
        else:
            clienteid = Cliente.objects.get(pk=id)
            formulario = ClienteForm(request.POST or None, request.FILES or None, instance=clienteid)
        if formulario.is_valid():
            formulario.save()
        return redirect('lista')

def eliminar(request, id):
    bc=Cliente.objects.get(id=id)
    bc.delete()
    return redirect('lista')
        
        
