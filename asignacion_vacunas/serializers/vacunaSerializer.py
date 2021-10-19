from asignacion_vacunas.models.vacuna import Vacuna
from rest_framework                   import serializers

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Vacuna
        fields = ['laboratorio_vacuna', 'cantidad', 'fecha_resolucion']

    def to_representation(self, obj):
        vacuna = Vacuna.objects.get(num_resolucion=obj.num_resolucion)
        return {
            'numero_resolucion'  : vacuna.num_resolucion,
            'laboratorio_vacuna' : vacuna.laboratorio_vacuna
        }