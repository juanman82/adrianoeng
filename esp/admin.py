from django.contrib import admin

from esp.models import Esp_inicio
from esp.models import Esp_nosotros
from esp.models import Esp_contacto
from esp.models import Esp_productos


class Esp_inicioAdmin(admin.ModelAdmin):
    fields =  ['titulo', 'contenido', 'publicado']

    admin.site.register(Esp_inicio)

class Esp_nosotrosAdmin(admin.ModelAdmin):
    fields =  ['titulo', 'contenido', 'publicado']

    admin.site.register(Esp_nosotros)

class Esp_contactoAdmin(admin.ModelAdmin):
    fields =  ['nombre', 'mensaje', 'email']

    admin.site.register(Esp_contacto)

class Esp_productosAdmin(admin.ModelAdmin):
    fields =  ['producto', 'imagen', 'descripcion']

    admin.site.register(Esp_productos)
