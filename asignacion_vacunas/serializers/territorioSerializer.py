from asignacion_vacunas.models.territorio                import Territorio
from asignacion_vacunas.models.asignacion                import Asignacion
from rest_framework                                      import serializers
from asignacion_vacunas.serializers.asignacionSerializer import AsignacionSerializer

class TerritorioSerializer(serializers.ModelSerializer):
    asignacion = AsignacionSerializer()
    class Meta:
        model = Territorio
        fields = ['cod_territorio', 'username', 'password', 'nom_territorio']

    def create(self, validated_data):
        asignacionData = validated_data.pop('nom_territorio')
        userInstance = Territorio.objects.create(**validated_data)
        Asignacion.objects.create(territorio=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        territorio = Territorio.objects.get(cod_territorio=obj.cod_territorio)
        asignacion = Asignacion.objects.get(territorio=obj.id)       
        return {
                    'codigo_territorio': territorio.codigo_territorio,
                    'username'         : territorio.username,
                    'nom_territorio'   : territorio.nom_territorio,                    
                    'asignacion'       : {
                        'id'                : asignacion.id,
                        'num_resolucion'    : vacuna.num_resolucion,
                        'fecha_resolucion'  : vacuna.fecha_resolucion,
                        'anio'              : asignacion.anio,
                        'laboratorio_vacuna': vacuna.laboratorio_vacuna,
                        'cantidad'          : vacuna.cantidad,
                        'uso_vacuna'        : asignacion.uso_vacuna,
                        'fecha_corte'       : asignacion.fecha_corte
                    }
                }
                