"""
Pharmacy model

Model to manage pharmacies
"""

# Django
from django.db import models

# Django Tenants
from django_tenants.models import TenantMixin, DomainMixin


class Pharmacy(TenantMixin):
    """
    Pharmacy model

    A pharmacy is an tenant in the system
    """
    PACKAGES = [
        ('STT', 'Starter'),
        ('STD', 'Standart'),
        ('PRM', 'Premium'),
    ]

    name = models.CharField(max_length=50)
    prefix = models.CharField(max_length=2)
    nit = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    package = models.CharField(max_length=3, choices=PACKAGES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    """
    Domain model

    A domain is used to manage subdomain and schema of tenant
    """
