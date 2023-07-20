from django.contrib.auth import get_user_model
from django.db import models

from jornada_milhas.accounts.models import CreationModificationBase

User = get_user_model()


class Post(CreationModificationBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    photo = models.ImageField()
    statement = models.TextField()

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.pk} - {self.user.name}"
