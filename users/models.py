from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# class CustomUser(models.Model):
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser)