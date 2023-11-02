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

    class Meta:
        model = Pet
        fields = ["name", "type", "owner", "created_at"]


class PetDateSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize pet date
    """

    class Meta:
        model = PetDate
        fields = ["datetime", "type", "email", "pet"]
