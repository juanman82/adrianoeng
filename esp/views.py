from django.shortcuts import render
from .models import Esp_inicio
from .models import Esp_productos




def esp_inicio(request):
    inicio = Esp_inicio.objects.get(publicado=True)
    titulo = inicio.titulo
    contenido = inicio.contenido
    descripcion = inicio.descripcion
    imagen = inicio.imagen
    context = {

        "temp_titulo": titulo,
        "temp_descripcion": descripcion,
        "temp_contenido": contenido,
        "temp_imagen": imagen,
    }
    return render(request, "espanol/inicio.html", context)


def esp_nosotros(request):
    titulo = Esp_productos.objects.get(publicado=True)

    contenido = titulo.contenido
    context = {

        "temp_titulo": titulo,
        "temp_contenido": contenido,
    }
    return render(request, "espanol/nosotros.html", context)


def home(request):
    return render(request, "espanol/inicio.html")