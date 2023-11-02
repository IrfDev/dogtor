from vet.models import PetOwner, Pet, PetDate
from rest_framework import serializers


# Serializers => Representation of our API
# This class already have the CRUD


class OnwerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize
    """

    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name", "email", "phone", "created_at"]


class PetSerialize(serializers.HyperlinkedModelSerializer):
    """
    Serialize Pet model
    """

    owner = serializers.PrimaryKeyRelatedField(
        queryset=PetOwner.objects.all(), many=False
    )

    class Meta:
        model = Pet
        fields = ["name", "type", "owner", "created_at"]


class PetDateSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize pet date
    """

    pet = serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all(), many=False)

    class Meta:
        model = PetDate
        fields = ["datetime", "type", "email", "pet"]


class OwnersListSerializer(serializers.ModelSerializer):
    """List serializer"""

    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name"]


# class OwnersDetailSerializer(serializers.ModelSerializer):
#     """Serializer for the of a Pet Owner"""

#     class Meta:
#         model = PetOwner
#         fields = "__all__"


# class OwnersCreateSerializer(serializers.ModelSerializer):
#     """Serializer for the of a Pet Owner"""

#     class Meta:
#         model = PetOwner
#         fields = ["first_name", "last_name", "email", "address", "phone"]


# class OwnersDestroySerializer(serializers.ModelSerializer):
#     """Serializer for destroying a Pet Owner"""

#     class Meta:
#         model = PetOwner
#         fields = "__all__"


# class OwnersCreateSerializer(serializers.ModelSerializer):
#     """Serializer for the of a Pet Owner"""

#     class Meta:
#         model = PetOwner
#         fields = ["first_name", "last_name", "email", "address", "phone"]


class OwnersCreateSerializer(serializers.ModelSerializer):
    """Serializer for the of a Pet Owner"""

    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name", "email", "address", "phone"]


class OwnersUpdateDestroyDetailSerializer(serializers.ModelSerializer):
    """Serializer for destroying a Pet Owner"""

    class Meta:
        model = PetOwner
        fields = "__all__"
