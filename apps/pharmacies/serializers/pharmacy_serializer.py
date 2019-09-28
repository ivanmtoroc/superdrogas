"""
Pharmacy serializer

Serializer to pharmacy model
"""

# Django Rest Framework
from rest_framework import serializers

# Pharmacies models
from apps.pharmacies.models import (
    Domain,
    Pharmacy
)

# Accounts utilities
from apps.accounts.utilities import create_superuser


class PharmacySerializer(serializers.ModelSerializer):
    """
    Pharmacy serializer

    Execute CRUD actions in the pharmacy model
    """
    class Meta:
        model = Pharmacy
        fields = '__all__'

    def create(self, validated_data):
        pharmacy = Pharmacy(**validated_data)
        pharmacy.save()
        domain = Domain(
            domain=f"{validated_data['schema_name']}.localhost",
            tenant_id=pharmacy.id,
        )
        domain.save()

        create_superuser(schema_name=pharmacy.schema_name, email=Pharmacy.email)

        return pharmacy
