"""""
Views for veterinaries
""" ""


from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
)
from vet.models import PetOwner, Pet
from vet.forms import PetOwnerForm, PetForm

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


# class PetList(TemplateView):
#     """
#     Listing pets list with a class view
#     """

#     template_name = "vet/pet/list.html"

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         pets = Pet.objects.all()

#         # It's always required to extend the context, rather than sending a new

#         context = super().get_context_data()

#         context["pets"] = pets

#         return context


class PetList(ListView):
    """
    Listing pets list with a class view
    """

    template_name = "vet/pet/list.html"
    model = PetOwner
    context_object_name = "pets"


# class PetDetail(TemplateView):
#     """
#     Listing pets list with a class view
#     """

#     template_name = "vet/pet/detail.html"

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         # Params are going to be binded to the kwargs
#         pet = Pet.objects.get(pk=kwargs["pk"])

#         context = super().get_context_data()

#         context["pet"] = pet

#         return context


class PetDetail(DetailView):
    """
    Listing pets list with a class view
    """

    template_name = "vet/pet/detail.html"
    model = Pet
    context_object_name = "pet"


class OwnersCreate(CreateView):
    """
    View for create new pet owners
    """

    # 1. Model
    # 2. Template
    # 3. Form
    # 4. Success url
    form_class = PetOwnerForm
    model = PetOwner
    template_name = "vet/owners/create.html"
    success_url = reverse_lazy("vet:owners_list")


class OwnersUpdate(UpdateView):
    """
    View for update pet owners
    """

    # 1. Model
    # 2. Template
    # 3. Form
    # 4. Success url
    model = PetOwner
    form_class = PetOwnerForm
    template_name = "vet/owners/update.html"
    success_url = reverse_lazy("vet:owners_list")


class PetsCreate(CreateView):
    """
    View for create new pet owners
    """

    # 1. Model
    # 2. Template
    # 3. Form
    # 4. Success url
    form_class = PetForm
    model = Pet
    template_name = "vet/pet/create.html"
    success_url = reverse_lazy("vet:pets_list")


class PetsUpdate(UpdateView):
    """
    View for create new pet owners
    """

    # 1. Model
    # 2. Template
    # 3. Form
    # 4. Success url
    form_class = PetForm
    model = Pet
    template_name = "vet/pet/update.html"
    success_url = reverse_lazy("vet:pets_list")
