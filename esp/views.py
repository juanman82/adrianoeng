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

def esp_productos(request):
    producto = Esp_productos.objects.get(publicado=True)
    imagen = Esp_productos.imagen
    descipcion = Esp_productos.descripcion
    context = {
        "temp_producto": producto,
        "temp_descripcion": descipcion,
        "temp_imagen": imagen,
    }
    return render(request, "espanol/inicio.html", context)


def home(request):
    return render(request, "espanol/productos.html")