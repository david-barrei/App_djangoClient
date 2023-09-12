from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def inicio(request):
    return render(request,'paginas_base/inicio.html')


def lista(request):
    clientes =Cliente.objects.all()
    return render(request,"Crud/listado.html",{"clientes":clientes})

def crear(request):
    if request.method=='GET':
        formulario=ClienteForm()
        return render (request,'Crud/crear.html', {'formulario':formulario})
    else:
        formulario=ClienteForm(request.POST)
        if formulario.is_valis():
            formulario.save()
            return redirect('lista')

        
        
