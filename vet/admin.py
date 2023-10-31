from django.contrib import admin


# Models
# from . import models -> importamos todos los modelos

# Importamos especificamente los modelos que le decimos
from vet.models import Pet, PetOwner

# Register your models here.


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    """Pet Admin model for admin."""

    fields = ["name"]
    fields = ["type"]
    fields = ["owner"]


@admin.register(PetOwner)
class PetAdmin(admin.ModelAdmin):
    """Pet Owner model for admin."""

    fields = ["first_name"]
    fields = ["last_name"]
    fields = ["address"]
    fields = ["email"]
    fields = ["phone"]


# SITIO -> Panel de administracion para la app de 'pet'
class BlogAdminArea(admin.AdminSite):
    """Pet admin panel administration."""

    site_header = "Vet Site Admin Area"


# Instanciar nuestra clase para poderla utilizar
blog_admin_site = BlogAdminArea(name="PetAdmin")
