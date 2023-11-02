from django.shortcuts import render
from rest_framework import viewsets
from vet.models import PetOwner, Pet, PetDate
from api.serializers import OnwerSerializer, PetDateSerializer, PetSerialize

# Create your views here.


class OwnersViewSet(viewsets.ModelViewSet):
    """Some"""

    # Queryset to use
    # Serializer

    queryset = PetOwner.objects.all()
    serializer_class = OnwerSerializer


class PetViewSets(viewsets.ModelViewSet):
    """Some"""

    # Queryset to use
    # Serializer

    queryset = Pet.objects.all()
    serializer_class = PetSerialize


class PetDateViewSets(viewsets.ModelViewSet):
    """Some"""

    # Queryset to use
    # Serializer

    queryset = PetDate.objects.all()
    serializer_class = PetDateSerializer
