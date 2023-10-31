from typing import Any
from django.shortcuts import render
from vet.models import PetOwner


# Generic views
from django.views.generic import TemplateView

# Create your views here.


def list_pet_owners(request):
    owners = PetOwner.objects.all()

    context = {"owners": owners}

    return render(request, "vet/owners/list.html", context)


# You'll need to add a property call template_name


# Also you'll need to redefine get_context_data to pass new keys to the context
class OwnersList(TemplateView):
    template_name = "vet/owners/list.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        owners = PetOwner.objects.all()

        context = super().get_context_data()

        context["owners"] = owners

        return context
