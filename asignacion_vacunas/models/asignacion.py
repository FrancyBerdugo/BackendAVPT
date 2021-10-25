from django.db               import models
from django.db.models.fields import AutoField
from .territorio             import Territorio

class Asignacion(models.Model):
    id                 = AutoField(primary_key=True)
    num_resolucion     = models.IntegerField(default=0)
    fecha_resolucion   = models.DateTimeField()
    anio               = models.IntegerField(default=0)
    cod_territorio     = models.ForeignKey(Territorio, related_name='territorio', on_delete=models.CASCADE)
    laboratorio_vacuna = models.CharField( max_length = 20)
    cantidad           = models.IntegerField(default=0)
    uso_vacuna         = models.CharField( max_length = 40)
    fecha_corte        = models.DateTimeField() 
    
