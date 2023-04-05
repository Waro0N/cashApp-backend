from django.db import models
from django.contrib.auth.models import User
from profiles.models import CustomUser
# Create your models here.
class Categories(models.Model):
    created_by = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        related_name='user_name',
        on_delete=models.CASCADE
    )

    category_name = models.CharField(max_length=50)


    def __str__(self):
        return self.category_name