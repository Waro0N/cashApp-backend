from django.db import models
from django.contrib.auth.models import User
from categories.models import Categories


# Create your models here.
class CashFlow(models.Model):
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='cash_user',
        on_delete=models.CASCADE
    )

    date = models.DateField()
    debit = models.IntegerField()
    credit = models.IntegerField()
    reason = models.CharField(max_length=150)
    category_dashboard = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return self.reason