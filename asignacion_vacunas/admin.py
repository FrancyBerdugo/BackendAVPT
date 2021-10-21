from django.contrib     import admin
from .models.asignacion import Asignacion
from .models.territorio import Territorio

admin.site.register(Asignacion)
admin.site.register(Territorio)

