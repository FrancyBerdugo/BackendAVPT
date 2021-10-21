from asignacion_vacunas.models.asignacion import Asignacion
from asignacion_vacunas.models.territorio import Territorio
from rest_framework                       import serializers

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Asignacion
        fields = ['num_resolucion','fecha_resolucion', 'anio', 'laboratorio_vacuna', 'cantidad', 'uso_vacuna', 'fecha_corte'] 

   