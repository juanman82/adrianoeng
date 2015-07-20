from django.shortcuts import render
from .models import Esp_inicio
from .models import Esp_nosotros
from .models import Esp_productos




def esp_inicio(request):
    # inicio = Esp_inicio.objects.get(publicado=True)
    # titulo = inicio.titulo
    # contenido = inicio.contenido
    # descripcion = inicio.descripcion
    # imagen = inicio.imagen
    queryset = Esp_inicio.objects.filter(publicado=1).order_by('-id')
    context = {

    "queryset": queryset

    }




    return render(request, "espanol/inicio.html", context)


def esp_nosotros(request):
    queryset = Esp_nosotros.objects.filter(publicado=1).order_by('-id')
    context = {

    "queryset": queryset

    }
    return render(request, "espanol/nosotros.html", context)

def esp_productos(request):
    queryset = Esp_productos.objects.filter(publicado=1).order_by('-id')
    context = {

    "queryset": queryset

    }

    return render(request, "espanol/productos.html", context)


