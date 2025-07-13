from django.db import models

# setting.py
# AUTH_USER_MODEL = "your_app_name.CustomUser"  #

# AUTHENTICATION_BACKENDS = [
#     "your_app_name.backends.EmailBackend",  # Path to your custom backend
#     "django.contrib.auth.backends.ModelBackend",
# ]


# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractUser
# from rest_framework.validators import ValidationError


# # Create your models here.
# # ==========================================================================
# # Custom user model for authentication for DRF
# # ==========================================================================
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     # def create_superuser(self, email, password, **extra_fields):
#     #     extra_fields.setdefault("is_staff", True)
#     #     extra_fields.setdefault("is_superuser", True)
#     #     if extra_fields.get("is_staff") is not True:
#     #         raise ValidationError("Superuser is has to have is_staff being true")
#     #     if extra_fields.get("is_superuser") is not True:
#     #         raise ValidationError("Superuser is has to have is_superuser being true")
#     #     return self.create_user(email=email, password=password, **extra_fields)


# class User(AbstractUser):
#     email = models.CharField(max_length=80, unique=True)
#     username = models.CharField(max_length=45)
#     date_of_birth = models.DateField(null=True)

#     objects = CustomUserManager()
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username"]

#     def __str__(self):
#         return self.username
