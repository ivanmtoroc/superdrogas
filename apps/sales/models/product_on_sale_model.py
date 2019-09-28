"""
Product on sale invoice model

Model to manage products on sale invoice
"""

# Django
from django.db import models

# Inventory models
from apps.inventory.models import Product

# Sales models
from .sale_invoice_model import SaleInvoice


class ProductOnSaleInvoice(models.Model):
    """
    ProductOnSaleInvoice model
    """
    sale_invoice_id = models.ForeignKey(SaleInvoice, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}: {self.product_id.name} - {self.quantity}'

    def product_name(self):
        """
        product_name return the name of the product category
        """
        return self.product_id.name

    def product_description(self):
        """
        product_name return the name of the product category
        """
        return self.product_id.description

    def product_total_price(self):
        """
        product_name return the name of the product category
        """
        return self.quantity * self.unit_price
