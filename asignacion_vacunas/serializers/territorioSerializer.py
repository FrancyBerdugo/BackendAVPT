from asignacion_vacunas.models.territorio import Territorio
from rest_framework                       import serializers

class Territorio(serializers.ModelSerializer):
    class Meta:
        model  = Territorio
        fields = ['nom_territorio']

    def to_representation(self, obj):
        territorio = Territorio.objects.get(cod_territorio=obj.cod_territorio)
        return {
            'codigo_territorio' : territorio.cod_territorio,
            'nombre_territorio' : territorio.nom_territorio
        }