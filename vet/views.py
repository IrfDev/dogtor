from django.shortcuts import render
from vet.models import PetOwner
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def list_pet_owners(request):
    owners = PetOwner.objects.all()

    context = {"owners": owners}

    return render(request, "vet/owners/list.html", context)
