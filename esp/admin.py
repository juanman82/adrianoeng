from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from esp.models import Esp_inicio
from esp.models import Esp_nosotros
from esp.models import Esp_contacto
from esp.models import Esp_productos
from esp.models import Esp_Servicios


class Esp_inicioAdmin(admin.ModelAdmin):
    fields =  ['titulo', 'contenido', 'publicado']

    admin.site.register(Esp_inicio, MarkdownModelAdmin)

class Esp_nosotrosAdmin(admin.ModelAdmin):
    fields =  ['titulo', 'descripcion','imagen', 'titulo2', 'descripcion2', 'titulop1', 'producto1', 'titulop2', 'producto2', 'titulop3', 'producto3' ,'publicado']







    admin.site.register(Esp_nosotros)

class Esp_contactoAdmin(admin.ModelAdmin):
    fields =  ['nombre', 'mensaje', 'email']

    admin.site.register(Esp_contacto)

class Esp_productosAdmin(admin.ModelAdmin):
    fields =  ['producto', 'imagen', 'descripcion']

    admin.site.register(Esp_productos)

class Esp_ServiciosAdmin(admin.ModelAdmin):
    fields =  ['producto',  'servicio', 'imagen', 'publicado',]

    admin.site.register(Esp_Servicios)

