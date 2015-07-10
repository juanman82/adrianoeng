from django.contrib import admin

from esp.models import Esp_inicio


class Esp_inicioAdmin(admin.ModelAdmin):
    fields =  ['titulo', 'contenido', 'publicado']

    admin.site.register(Esp_inicio)

