"""
ProductOnSaleInvoice serializer

Serializer to ProductOnSaleInvoice model
"""

# Django Rest Framework
from rest_framework import serializers

# Sales models
from apps.sales.models import ProductOnSaleInvoice


class ProductOnSaleInvoiceSerializer(serializers.ModelSerializer):
    """
    ProductOnSaleInvoice serializer

    Execute CRUD actions in the ProductOnSaleInvoice model
    """
    class Meta:
        model = ProductOnSaleInvoice
        fields = (
            'sale_invoice_id',
            'product_id',
            'product_name',
            'product_description',
            'product_total_price',
            'quantity',
            'unit_price',
            'is_active',
        )
