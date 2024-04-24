from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def create_user(
            self,
            username=None,
            email=None,
            password=None,
            **extra_fields
    ):
        if not email:
            raise ValueError("The given email must be set")
        if not username:
            username = email
        return super().create_user(
            username,
            email,
            password,
            **extra_fields
        )

    def create_superuser(
            self,
            username=None,
            email=None,
            password=None,
            **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        if not username:
            username = email
        return super().create_superuser(
            username,
            email,
            password,
            **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(
        'Адрес электронной почты',
        unique=True,
    )
    username = models.CharField(
        max_length=150,
        blank=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
