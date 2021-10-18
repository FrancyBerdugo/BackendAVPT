from django.contrib     import admin
from .models.asignacion import Asignacion
from .models.territorio import Territorio
from .models.vacuna     import Vacuna

admin.site.register(Asignacion)
admin.site.register(Territorio)
admin.site.register(Vacuna)
# Register your models here.
