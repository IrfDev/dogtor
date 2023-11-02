from vet.models import PetOwner
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
