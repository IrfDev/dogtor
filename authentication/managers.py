# A manager encapsulates database query logic

from django.contrib.auth.models import BaseUserManager


class ModUserManager(BaseUserManager):
    """
    Custom Manager for ModUser
    """

    # Two methods that we always used
    # 1. create_user
    # 2. create_superuser

    def create_user(self, email, user_name, first_name, password, **other_fields):
        """
        Overrided create_user func
        """

        if not email:
            raise ValueError("You must provide an email")

        email = self.normalize_email(email)

        user = self.model(
            email=email, user_name=user_name, first_name=first_name, **other_fields
        )

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        """
        Overrided create super user
        """

        # First of all we need to set the defaults

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_superuser", True)

        # We can always reuse the create_user function
        self.create_user(email, user_name, first_name, password, **other_fields)

        return self
