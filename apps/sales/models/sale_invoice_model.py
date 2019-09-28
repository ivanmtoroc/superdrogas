"""
Sales model

Model to manage commerce
"""

# Django
from django.db import models

# Accounts models
from apps.accounts.models.user_model import User


class SaleInvoice(models.Model):
    """
    SaleInvoice model
    """

    SALE_TYPES = [
        ('OL', 'Online'),
        ('OS', 'On-site')
    ]

    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
    client_id = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE)
    sale_type = models.CharField(max_length=2, choices=SALE_TYPES)
    date = models.DateField(auto_now=True)
    total_amount = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}: {self.client_id.username} - {self.date}'
