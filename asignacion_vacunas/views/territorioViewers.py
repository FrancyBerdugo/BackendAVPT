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

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

class TerritorioAsignacionView(generics.ListAPIView):
    serializer_class   = TerritorioSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

class TerritorioCreateView(generics.CreateAPIView):
    serializer_class   = TerritorioSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
                       
        serializer = TerritorioSerializer(data=request.data['transaction_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

class TerritorioUpdateView(generics.UpdateAPIView):
    serializer_class   = TerritorioSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Territorio.objects.all()

    def update(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

class TerritorioDeleteView(generics.DestroyAPIView):
    serializer_class   = TerritorioSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Territorio.objects.all()

    def deliete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
           