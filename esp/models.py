from django.db import models
from django_markdown.models import MarkdownField



# Create your models here.
class Esp_inicio(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descripcion = MarkdownField(null=True)
    imagen = models.ImageField(null=True)
    contenido = MarkdownField(null=True)
    publicado = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Inicio"

    def __str__(self):
        titulo = self.titulo
        return titulo



class Esp_nosotros(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descripcion = MarkdownField(null=True)
    imagen = models.ImageField(null=True)
    contenido = MarkdownField(null=True)
    publicado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        titulo = self.titulo
        return titulo


class Esp_contacto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    mensaje = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    class Meta:
        verbose_name_plural = 'Contacto'

    def __str__(self):
        mensaje = self.cleaned_data.get('mensaje')
        return mensaje


class Esp_productos(models.Model):
    producto = models.CharField(max_length=100, null=False)
    imagen = models.ImageField(null=True)
    descripcion = MarkdownField(null=True)
    publicado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        producto = self.producto
        return producto
