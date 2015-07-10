from django.db import models

# Create your models here.
class Esp_inicio(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    publicado = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Inicio'

    def __str__(self):
        titulo = self.titulo
        return titulo



class Esp_nosotros(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    publicado = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        titulo = self.titulo
        return titulo


class Esp_contacto(models.Model):
    nombre = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    class Meta:
        verbose_name_plural = 'Contacto'

    def __str__(self):
        titulo = self.cleaned_data.get('nombre')
        return titulo


class Esp_productos(models.Model):
    producto = models.CharField(max_length=100)
    imagen = models.ImageField
    descripcion = models.TextField
    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        titulo = self.nombre
        return titulo
