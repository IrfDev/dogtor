from django import forms
from vet.models import PetOwner, Pet


class PetOwnerForm(forms.ModelForm):
    # 1. Model
    # 2. Fields inside our form
    # Both needs to be included in fields

    class Meta:
        model = PetOwner
        fields = ("first_name", "last_name", "address", "email", "phone")


class PetForm(forms.ModelForm):
    # 1. Model
    # 2. Fields inside our form
    # Both needs to be included in fields

    class Meta:
        model = Pet
        fields = ("name", "type", "owner")
