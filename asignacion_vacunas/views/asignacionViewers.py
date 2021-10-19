from django.conf                       import settings
from rest_framework                    import generics, status
from rest_framework.response           import Response
from rest_framework.permissions        import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
               
from asignacion_vacunas.models.asignacion                import Asignacion
from asignacion_vacunas.serializers.asignacionSerializer import AsignacionSerializer

class AsignacionDetailView(generics.RetrieveAPIView):
    queryset         = Asignacion.objects.all()
    serializer_class = AsignacionSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        #return super().get(request. *args, **kwargs)