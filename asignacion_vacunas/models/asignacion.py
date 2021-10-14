from django.db   import models
from django.db.models.fields import AutoField
from .territorio import Territorio
from .vacuna     import Vacuna

class Asignacion(models.Model):
    id                 = AutoField(primary_key=True)
    num_resolucion     = models.IntegerField(primary_key=True)
    fecha_resolucion   = models.DateTimeField()
    anio               = models.IntegerField(default=0)
    cod_territorio     = models.IntegerField(primary_key=True)
    nom_territorio     = models.CharField( max_length = 20)
    laboratorio_vacuna = models.CharField( max_length = 20)
    cantidad           = models.IntegerField(default=0)
    uso_vacuna         = models.CharField( max_length = 40)
    fecha_corte        = models.DateTimeField() 

