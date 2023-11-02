# Class Based views

Are views with Class syntas.

Advantages: They have all the predefined methods and properties to add the different handlers


[Summarized docs](https://ccbv.co.uk/)




# Reverse Urls:

You can create reverse URL's to include on your templates.

Which is a set of functions to get the vet urls


# Forms

Forms for each Model. Each form needs to be associated with a DB Model. They're going to be handled on the frontend but described on backend

We have generic forms and template forms.

Each one can make based operations.

You can find more on class based views


# Admin

You can customize your admin, and also the entities that are available in the admin panel

For each entity whose going to be added you should create a group role so you can protect your entities

## Permissions in routes:

The permissions you've created are editable on admin but needs to be apply on each view with the built-in Mixin: `PermissionRequiredMixin`.
Mixin to protect the view 
And then in your class you'll need to include the property `permission_required` with the following syntax: 

````python
"APP.OPERATION_ENTITY"


# E.G

"vet.change_pet"

# Where "vet" is the name of the app "change" is the operation and "pet" is the entity
````

````python 
# Class view with PermissionRequiredMixin

class PetsUpdate(PermissionRequiredMixin, UpdateView):
    """
    View for create new pet owners
    """

    # 1. Model
    # 2. Template
    # 3. Form
    # 4. Success url
    permission_required = "vet.change_pet"
    form_class = PetForm
    model = Pet
    template_name = "vet/pet/update.html"
    success_url = reverse_lazy("vet:pets_list")

````


### Mixins:
Way to reuse code and share: properties and methods to class instances.

On views, you can add custom functionallity to your class with Mixins


# Admin authentication

## Redirect url's:

````python
# After login you'll be redirected to:
LOGIN_REDIRECT_URL = "vet/owners"
# After logout you'll be redirected to:
LOGOUT_REDIRECT_URL = "/"
````
## Auth urls:

You need to include the admin url's from `django.contrib.auth.urls`:

````python
urlpatterns=[
  # ...
  path("accounts/", include("django.contrib.auth.urls")),
]
````



# Create Custom User Model extended from django.admin

Most of the time the first thing you'll do when  you create a new project is create a custom user model



# Rest framework

You can include views, serializers and urls

Views you can include viewsets for default API documentation and management. 

You can also use generic views, just as you can with 

[Summarized docs on classes for Django](https://www.cdrf.co/)

Serializers how are you resolving the different models

