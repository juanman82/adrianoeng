from django.shortcuts import render
from .models import Esp_inicio



def esp_inicio(request):
    titulo = Esp_inicio.objects.get(publicado=True)

    contenido = titulo.contenido
    context = {

        "temp_titulo": titulo,
        "temp_contenido": contenido,
    }
    return render(request, "espanol/inicio.html", context)


def esp_nosotros(request):
    return render(request, "espanol/nosotros.html")


def home(request):
    return render(request, "espanol/inicio.html")