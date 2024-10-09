from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
class User(AbstractUser):

    password = models.CharField(max_length=128)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"access": str(refresh.access_token), "refresh": str(refresh)}

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"