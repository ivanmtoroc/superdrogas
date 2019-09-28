"""
Sales URLs

The 'urlpatterns' list routes URLs to viewsets
"""

# Django Rest Framework
from rest_framework import routers

# Sales viewsets
from .viewsets.sale_invoice_viewset import SaleInvoiceViewSet
from .viewsets.product_on_sale_viewset import ProductOnSaleInvoiceViewSet

# Invoices
from .utilities import generar_factura_xml, generar_factura_pdf, sales_report, general_pdf_report
from .reports import get_products_report
from django.conf.urls import url
from .reports import get_sales_report

ROUTER = routers.DefaultRouter()

ROUTER.register(r'sales_invoice', SaleInvoiceViewSet)
ROUTER.register(r'product_on_sale', ProductOnSaleInvoiceViewSet)

urlpatterns = [
    url('xml', generar_factura_xml, name='xml'),
    url('general_pdf_report', general_pdf_report, name='general_pdf_report'),
    url('pdf', generar_factura_pdf, name='pdf'),
    url('sales_report/', sales_report, name='sales_report'),
    url('products_report', get_products_report, name='get_products_report'),
    url('get_sales_report', get_sales_report, name='get_sales_report')

]

urlpatterns += ROUTER.urls
