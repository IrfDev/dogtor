from rest_framework import viewsets, generics
from vet.models import PetOwner, Pet, PetDate
from api.serializers import (
    OwnersCreateSerializer,
    OwnersUpdateDestroyDetailSerializer,
)


# Create your views here.


# class OwnersViewSet(viewsets.ModelViewSet):
#     """Some"""

#     # Queryset to use
#     # Serializer

#     queryset = PetOwner.objects.all()
#     serializer_class = OnwerSerializer


# class PetViewSets(viewsets.ModelViewSet):
#     """Some"""

#     # Queryset to use
#     # Serializer

#     queryset = Pet.objects.all()
#     serializer_class = PetSerialize


# class PetDateViewSets(viewsets.ModelViewSet):
#     """Some"""

#     # Queryset to use
#     # Serializer

#     queryset = PetDate.objects.all()
#     serializer_class = PetDateSerializer


# class ListOwnerAPIView(generics.ListAPIView):
#     queryset = PetOwner.objects.all().order_by("created_at")
#     serializer_class = OwnersListSerializer


# class RetrieveOwnerAPIView(generics.RetrieveAPIView):
#     """Detail Pet Owener Api view"""

#     queryset = PetOwner.objects.all().order_by("created_at")
#     serializer_class = OwnersDetailSerializer


class CreateListOwnerAPIView(generics.ListCreateAPIView):
    """Detail Pet Owener Api view"""

    queryset = PetOwner.objects.all()
    serializer_class = OwnersCreateSerializer


class DestroyUpdateOwnerAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Detail Pet Owener Api view"""

    queryset = PetOwner.objects.all()
    serializer_class = OwnersUpdateDestroyDetailSerializer
