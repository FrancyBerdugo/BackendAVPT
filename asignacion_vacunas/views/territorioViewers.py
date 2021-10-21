from django.conf                                         import settings
from rest_framework                                      import generics, status
from rest_framework.response                             import Response
from rest_framework.permissions                          import IsAuthenticated
from rest_framework_simplejwt.backends                   import TokenBackend

from asignacion_vacunas.models.territorio                import Territorio
from asignacion_vacunas.models.asignacion                import Asignacion
from asignacion_vacunas.serializers.territorioSerializer import TerritorioSerializer

class TerritorioDetailView(generics.RetrieveAPIView):
    serializer_class   = TerritorioSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Territorio.objects.all()

class TerritorioCreateView(generics.CreateAPIView):
    serializer_class   = TerritorioSerializer
    permission_classes = (IsAuthenticated,)