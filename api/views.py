from django.shortcuts import render
from rest_framework import viewsets
from vet.models import PetOwner
from api.serializers import OnwerSerializer

# Create your views here.


class OwnersViewSet(viewsets.ModelViewSet):
    """Some"""

    # Queryset to use
    # Serializer

    queryset = PetOwner.objects.all()
    serializer_class = OnwerSerializer
