from django.db import models

# Create your models here.
class Esp_inicio(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=30)

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        return titulo

class Esp_nosotros(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=30)

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        return titulo
class Esp_contacto(models.Model):
    nommbre = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=30)
    email = models.EmailField(null=False)

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        return titulo