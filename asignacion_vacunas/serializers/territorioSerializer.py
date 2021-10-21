from asignacion_vacunas.models.territorio                import Territorio
from asignacion_vacunas.models.asignacion                import Asignacion
from rest_framework                                      import serializers
from asignacion_vacunas.serializers.asignacionSerializer import AsignacionSerializer

class TerritorioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Territorio
        fields = ['cod_territorio', 'username', 'password', 'nom_territorio']

    def create(self, validated_data):       
        userInstance = Territorio.objects.create(**validated_data)        
        return userInstance

    def to_representation(self, obj):
        territorio = Territorio.objects.get(cod_territorio=obj.cod_territorio)
               
        return {
            'codigo_territorio': territorio.codigo_territorio,
            'username'         : territorio.username,
            'nom_territorio'   : territorio.nom_territorio,                      
            }
                