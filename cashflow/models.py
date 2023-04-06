from django.db import models
from django.contrib.auth.models import User
from categories.models import Categories
from profiles.models import CustomUser

# Create your models here.
class CashFlow(models.Model):
    created_by = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        related_name='cash_user',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    debit = models.IntegerField(null=True, blank=True)
    credit = models.IntegerField(null=True, blank=True)
    reason = models.CharField(max_length=150, null=True, blank=True)
    category_dashboard = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return self.reason