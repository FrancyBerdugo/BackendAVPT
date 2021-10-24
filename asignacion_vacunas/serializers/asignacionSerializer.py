from asignacion_vacunas.models.asignacion import Asignacion
from asignacion_vacunas.models.territorio import Territorio
from rest_framework                       import serializers

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Asignacion
        fields = ['num_resolucion','fecha_resolucion', 'anio', 'laboratorio_vacuna', 'cantidad', 'uso_vacuna', 'fecha_corte'] 

    def to_representation(self, obj):        
        territorio = Territorio.objects.get(cod_territorio=obj.territorio_cod_territorio)
        asignacion = Asignacion.objects.get(id=obj.id)
        
        return {
            'num_resolucion'    : asignacion.num_resolucion,   
            'fecha_resolucion'  : asignacion.fecha_resolucion, 
            'anio'              : asignacion.anio,             
            'laboratorio_vacuna': asignacion.laboratorio_vacuna,
            'cantidad'          : asignacion.cantidad,         
            'uso_vacuna'        : asignacion.uso_vacuna,        
            'fecha_corte'       : asignacion.fecha_corte,                            
            'territorio':{
                'cod_territorio': territorio.cod_territorio,
                'username'      : territorio.username,
                'nom_territorio': territorio.nom_territorio                
            }
        }

   