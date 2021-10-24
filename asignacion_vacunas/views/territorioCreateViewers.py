from rest_framework                                      import status, views
from rest_framework.response                             import Response
from rest_framework_simplejwt.serializers                import TokenObtainPairSerializer
from asignacion_vacunas.serializers.territorioSerializer import TerritorioSerializer

class TerritorioCreateView(views.APIView):

    def -(self, request, *args, **kwargs):
        serializer = TerritorioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"], 
                     "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
                
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)