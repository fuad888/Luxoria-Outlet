
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    image = models.FileField(upload_to='profile_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    