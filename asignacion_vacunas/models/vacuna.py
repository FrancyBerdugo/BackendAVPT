from django.db import models

class Vacuna(models.Model):
    num_resolucion     = models.IntegerField(primary_key=True)
    laboratorio_vacuna = models.CharField( max_length = 20)
    cantidad           = models.IntegerField(default=0)
    fecha_resolucion   = models.DateTimeField()