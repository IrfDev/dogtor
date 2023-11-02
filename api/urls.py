from django.urls import path, include

from api.views import OwnersViewSet


from rest_framework import routers


router = routers.DefaultRouter()


router.register("owners", OwnersViewSet)


urlpatterns = [path("", include(router.urls))]
