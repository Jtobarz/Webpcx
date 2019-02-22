from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import NuevaNot, UserLog
from .forms import NuevaNoti, LogU

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Contacto(request):
    return render(request, 'Contacto.html')

def Servicios(request):
    return render(request, 'Servicios.html')

def Gracias(request):
    return render(request, 'Gracias.html')

def jovenes(request):
    return render(request, 'jovenes-intentaron-destruir-camara-de-seguridad-en-plaza-de-las-condes.html')

def nuevo(request):
    return render(request, 'nuevo-boton-de-emergencia.html')

def enviar(request):
    return render(request, 'enviar.php')

def ingresar(request):
    if request.method=='POST':
        form = NuevaNoti(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('Webpcx:Noticias')
    else:
        form=NuevaNoti()
    return render(request, 'ingresar.html', {'form':form})


def Noticias(request):
    Webpcx = NuevaNot.objects.all().order_by('-fecha','-id')
    return render(request, 'Noticias.html', {'list':Webpcx})

def LogSec(request):
    if request.method=='GET':
        form = LogU(request.GET)
        if form.is_valid():
            post.author = request.user
        return redirect('Webpcx.ingresar')
    else:
        form=LogU()
    return render(request,'LogSec.html',{'form':form})
