"""""
Views for veterinaries
""" ""


from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from vet.models import PetOwner


# Generic views

# Create your views here.


def list_pet_owners(request):
    """_summary_
    Listing pet owners with a func view
    """
    owners = PetOwner.objects.all()

    context = {"owners": owners}

    return render(request, "vet/owners/list.html", context)


# You'll need to add a property call template_name


# Also you'll need to redefine get_context_data to pass new keys to the context
# class OwnersList(TemplateView):
#     """
#     Listing pet owners list with a class view
#     """

#     template_name = "vet/owners/list.html"

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         owners = PetOwner.objects.all()

#         # It's always required to extend the context, rather than sending a new

#         context = super().get_context_data()

#         context["owners"] = owners

#         return context


class OwnersList(ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"
