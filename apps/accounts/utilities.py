"""
Accounts app utilities
"""

# Django Tenants
from django_tenants.utils import schema_context

# Accounts models
from apps.accounts.models import User

# Sales model
from apps.sales.models.sale_invoice_model import SaleInvoice

# Django
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Sum

# Utilities
from superdrogas.utilities import random_password, send_admin_email


def create_superuser(schema_name, email):
    """
    create_superuser create the admin in new tenant
    """
    password = random_password()

    with schema_context(schema_name):
        User.objects.create_user(username='admin', password=password)

    send_admin_email('admin', password, email)


def get_backup(request):
    """
    get database backup from a pharmacy based on it's schema name
    """
    if request.method == 'GET':
        schema_name = request.GET.get('schema_name')

    command = 'tenant_command dumpdata'
    manage = os.path.join(settings.BASE_DIR, 'manage.py')
    path = f'media/{schema_name}.json'

    output = open(path, 'w+')
    os.system(f'{manage} {command} --schema={schema_name} --indent=4 > {path}')
    output.close()

    fs = FileSystemStorage('')
    with fs.open(path) as json:
        response = HttpResponse(json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="' + schema_name + '.json"'
        return response


def get_tenant_report(request):
    if request.method == 'GET':
        schema_name = request.GET.get('schema_name')

    response = {}

    with schema_context(schema_name):
        clients = User.objects.filter(rol='CM').count()
        response.update({'clients': clients})

        sellers = User.objects.filter(rol='SL').count()
        response.update({'sellers': sellers})

        admins = User.objects.filter(rol='AD').count()
        response.update({'admins': admins})

        online_sales = SaleInvoice.objects.filter(sale_type='OL').count()
        response.update({'online_sales': online_sales})

        online_sales_total_amount = SaleInvoice.objects.filter(sale_type='OL').aggregate(Sum('total_amount'))
        response.update({'online_sales_total_amount': online_sales_total_amount['total_amount__sum']})

    return JsonResponse(response)
