"""
SaleInvoice serializer

Serializer to SaleInvoice model
"""

# Django Rest Framework
from rest_framework import serializers

# Sales models
from apps.sales.models import SaleInvoice


class SaleInvoiceSerializer(serializers.ModelSerializer):
    """
    SaleInvoice serializer

    Execute CRUD actions in the SaleInvoice model
    """
    class Meta:
        model = SaleInvoice
        fields = '__all__'
