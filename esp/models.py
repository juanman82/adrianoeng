from django.db import models

# Create your models here.
class Esp_inicio(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=30)
    publicado = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Inicio'

    def __str__(self):
        titulo = self.titulo
        return titulo



class Esp_nosotros(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=30)
    publicado = models.BooleanField(default=True)

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        return titulo
    class Meta:
            verbose_name_plural = "Nosotros"


class Esp_contacto(models.Model):
    nombre = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=30)
    email = models.EmailField(null=False)

    def clean_titulo(self):
        titulo = self.cleaned_data.get('nombre')
        return titulo
    class Meta:
            verbose_name_plural = "Contacto"