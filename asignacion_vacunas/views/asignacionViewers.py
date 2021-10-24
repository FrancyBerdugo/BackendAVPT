from django.conf                        import settings
from rest_framework                     import generics, status
from rest_framework.response            import Response
from rest_framework.permissions         import IsAuthenticated
from rest_framework_simplejwt.backends  import TokenBackend

from asignacion_vacunas.models.asignacion                import Asignacion
from asignacion_vacunas.serializers.asignacionSerializer import AsignacionSerializer


class AsignacionTerritorioView(generics.ListAPIView):
    serializer_class   =  AsignacionSerializer
    permission_classes =  (IsAuthenticated, )

    def get_queryset(self):                  
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify = False)

        if valid_data['territorio_cod_territorio'] != self.kwargs['territorio']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)
        
        queryset = Asignacion.objects.filter(territorio_cod_territorio = self.kwargs['cod_territorio'])
        return queryset 

    
class AsignacionCreateView(generics.CreateAPIView):
    serializer_class   =  AsignacionSerializer
    permission_classes =  (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        print("Request:", request)
        print("Args:", args)
        print("KWArgs:", kwargs)
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token, verify = False)

        if valid_data['territorio_cod_territorio'] != request.data['territorio_cod_territorio']:
            stringResponse = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)

        serializer = AsignacionSerializer(data = request.data['Asignacion_data'])
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response("Asignado anteriormente", status = status.HTTP_201_CREATED)

    
class AsignacionUpdateView(generics.UpdateAPIView):
    serializer_class    = AsignacionSerializer
    permission_classes  = (IsAuthenticated, )
    queryset            = Asignacion.objects.all()

    def put(self, request, *args, **kwargs):
        print("Request:", request)
        print("Args:", args)
        print("KWArgs:", kwargs)
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token, verify = False)

        if valid_data['territorio_cod_territorio'] != request.data['territorio_cod_territorio']:
            stringResponse = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_404_UNAUTHORIZED)
        
        return super().update(request, *args, **kwargs)


class AsignacionDeleteView(generics.DestroyAPIView):
    serializer_class    =   AsignacionSerializer
    permission_classes  =   (IsAuthenticated, )
    queryset            =   Asignacion.objects.all()

    def delete(self, request, *args, **kwargs):
        print("Request:", request)
        print("Args:", args)
        print("Kwargs:", kwargs)
        token           = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend    = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data      = tokenBackend.decode(token, verify = False)

        if valid_data['territorio_cod_territorio'] != request.data['territorio_cod_territorio']:
            stringResponse  = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)