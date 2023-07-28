from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from jornada_milhas.accounts.models import CreationModificationBase

User = get_user_model()


class Post(CreationModificationBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    photo = models.ImageField(upload_to="post")
    statement = models.TextField()

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.pk} - {self.user.name}"


class Destination(CreationModificationBase):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="destination")
    price = models.DecimalField(max_digits=14, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))])

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name
