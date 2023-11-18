from rest_framework import viewsets, generics
from .serializer import PersonaSerializer
from .models import Persona

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    # permission_classes = [IsAuthenticated]


# class PersonaList(generics.ListCreateAPIView):
#     queryset = Persona.objects.all()
#     serializer_class = PersonaSerializer
#     permission_classes = [IsAuthenticated]
