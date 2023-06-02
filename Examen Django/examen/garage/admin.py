from django.contrib import admin

from .models import Contrato, Automovil, Caracteristica

admin.site.register(Contrato)
admin.site.register(Caracteristica)
admin.site.register(Automovil)
