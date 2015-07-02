from django.shortcuts import render



def esp_inicio(request):
    return render(request, "espanol/inicio.html")


def home(request):
    return render(request, "perfil/index.html")