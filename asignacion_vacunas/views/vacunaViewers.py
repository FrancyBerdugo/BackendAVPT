from django.conf                                     import settings
from rest_framework                                  import generics, status
from rest_framework.response                         import Response
from rest_framework.permissions                      import IsAuthenticated
from rest_framework_simplejwt.backends               import TokenBackend

from asignacion_vacunas.models.vacuna                import Vacuna
from asignacion_vacunas.models.asignacion            import Asignacion
from asignacion_vacunas.serializers.vacunaSerializer import VacunaSerializer
from asignacion_vacunas.serializers.asignacionSerializer import AsignacionSerializer

class VacunaDetailView(generics.RetrieveAPIView):
    serializer_class   = VacunaSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Vacuna.objects.all()

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

class VacunaAsignacionView(generics.ListAPIView):
    serializer_class   = VacunaSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

class VacunaCreateView(generics.CreateAPIView):
    serializer_class   = VacunaSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
                       
        serializer = VacunaSerializer(data=request.data['transaction_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

class VacunaUpdateView(generics.UpdateAPIView):
    serializer_class   = VacunaSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Vacuna.objects.all()

    def update(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

class VacunaDeleteView(generics.DestroyAPIView):
    serializer_class   = VacunaSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Vacuna.objects.all()

    def deliete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
           