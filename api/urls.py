from django.urls import path, include

from api.views import OwnersViewSet, PetViewSets, PetDateViewSets


from rest_framework import routers


router = routers.DefaultRouter()


router.register("owners", OwnersViewSet)
router.register("pets", PetViewSets)
router.register("pet-dates", PetDateViewSets)


urlpatterns = [path("", include(router.urls))]
