"""""
Views for veterinaries
""" ""


from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from vet.models import PetOwner, Pet


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
    # Under the hood is already calling the model.objects.all(). We're just setting the object name
    context_object_name = "owners"


class OwnerDetail(DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    # Under the hood is already calling the model.objects.all(). We're just setting the object name
    slug_field = "pk"
    context_object_name = "owner"


class PetList(TemplateView):
    """
    Listing pets list with a class view
    """

    template_name = "vet/pet/list.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        pets = Pet.objects.all()

        # It's always required to extend the context, rather than sending a new

        context = super().get_context_data()

        context["pets"] = pets

        return context


class PetDetail(TemplateView):
    """
    Listing pets list with a class view
    """

    template_name = "vet/pet/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # Params are going to be binded to the kwargs
        pet = Pet.objects.get(pk=kwargs["pk"])

        context = super().get_context_data()

        context["pet"] = pet

        return context
