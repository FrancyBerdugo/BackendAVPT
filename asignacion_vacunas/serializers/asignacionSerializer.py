from asignacion_vacunas.models.asignacion import Asignacion
from asignacion_vacunas.models.
from francy.asignacion_vacunas.models.territorio import Territorio
from francy.asignacion_vacunas.models.vacuna import Vacuna
from rest_framework                       import serializers

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Asignacion
        fields = ['num_resolucion','fecha_resolucion', 'anio', 'cod_territorio', 'nom_territorio', 'laboratorio_vacuna', 'cantidad', 'uso_vacuna', 'fecha_corte'] 

    def to_representation(self, obj):
        vacuna     = Vacuna.objects.get(num_resolucion=obj.num_resolucion_id)
        territorio = Territorio.objects.get(cod_territorio=obj.cod_territorio_id)
        asignacion = Asignacion.objects.get(id=obj.id)
        return {
            'id'         : asignacion.id,
            'anio'       : asignacion.anio,
            'uso_vacuna' : asignacion.uso_vacuna,
            'cantidad'   : asignacion.cantidad,
            'fecha_corte': asignacion.fecha_corte,
            'territorio' : {
                'codigo_territorio': territorio.codigo_territorio,
                'nom_territorio'   : territorio.nom_territorio
            },
            'vacuna' : {
                 'num_resolucion'    : vacuna.num_resolucion,
                 'laboratorio_vacuna': vacuna.laboratorio_vacuna,
                 'cantidad'          : vacuna.cantidad,
                 'fecha_resolucion'  : vacuna.fecha_resolucion
            }
            

        }