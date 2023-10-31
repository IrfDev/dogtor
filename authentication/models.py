from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from authentication.managers import ModUserManager


class ModUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom Moderator User
    """

    objects = ModUserManager()
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, unique=True)
    start_date = models.DateTimeField(auto_now_add=True)
    about = models.TextField(max_length=500)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Identifier field
    USERNAME_FIELD = "email"

    # Required fields to create a superuser
    # This fields are the ones whose going to be prompted after trying to create a new superuser

    REQUIRED_FIELDS = ["user_name", "first_name"]

    def __str__(self):
        return f"{self.user_name} {self.email}"
