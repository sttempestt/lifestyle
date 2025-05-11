from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",  # Изменённый related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions_set",  # Изменённый related_name
        blank=True
    )
    
    def __str__(self):
        return self.username