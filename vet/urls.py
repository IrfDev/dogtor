"""
URL configuration for dogtor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vet.views import (
    list_pet_owners,
    OwnersList,
    OwnerDetail,
    PetDetail,
    PetList,
    OwnersCreate,
    PetsCreate,
    OwnersUpdate,
    PetsUpdate,
)

urlpatterns = [
    # path("owners/", list_pet_owners,name="owners"),
    path("owners/", OwnersList.as_view(), name="owners_list"),
    path("owners/<int:pk>/", OwnerDetail.as_view(), name="owner_detail"),
    path("owners/add/", OwnersCreate.as_view(), name="pets_create"),
    path("owners/<int:pk>/edit/", OwnersUpdate.as_view(), name="owners_update"),
    path("pets/<int:pk>/", PetDetail.as_view(), name="pets_detail"),
    path("pets/", PetList.as_view(), name="pets_list"),
    path("pets/add/", PetsCreate.as_view(), name="pets_create"),
    path("pets/<int:pk>/edit/", PetsUpdate.as_view(), name="pets_update"),
]
