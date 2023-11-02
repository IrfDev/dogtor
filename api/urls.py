from django.urls import path, include

from api.views import CreateListOwnerAPIView, DestroyUpdateOwnerAPIView


from rest_framework import routers


router = routers.DefaultRouter()


# router.register("pets", PetViewSets)
# router.register("pet-dates", PetDateViewSets)


# urlpatterns = [
#     path("owners/", ListOwnerAPIView.as_view(), name="list_owners"),
#     path("owners/<int:pk>/", RetrieveOwnerAPIView.as_view(), name="retrieve_owner"),
#     path("owners/<int:pk>/update", UpdateOwnerAPIView.as_view(), name="update_owner"),
#     path(
#         "owners/<int:pk>/destroy", DestroyOwnerAPIView.as_view(), name="destroy_owner"
#     ),
#     path("owners/create", CreateOwnerAPIView.as_view(), name="create_owner"),
# ]

urlpatterns = [
    path("owners/", CreateListOwnerAPIView.as_view(), name="list_owners"),
    path(
        "owners/<int:pk>/", DestroyUpdateOwnerAPIView.as_view(), name="retrieve_owner"
    ),
]
