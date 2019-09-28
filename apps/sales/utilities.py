"""
Sales utilities
"""

# Django Tenants
from django_tenants.utils import schema_context

# String
from string import Template

# Django
from django.core import signing
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Sum
from django.db.models import Count
from apps.sales.models.product_on_sale_model import ProductOnSaleInvoice
from apps.inventory.models.product_model import Product
from superdrogas.utilities import get_tenant_info

# Accounts models
from apps.accounts.models import User

# Sales model
from apps.sales.models.sale_invoice_model import SaleInvoice

# XHTML2PDF
from xhtml2pdf import pisa

# String
from string import Template

# Python
import os

# Sales models
from .models import SaleInvoice, ProductOnSaleInvoice


@csrf_exempt
def generar_factura_xml(request):
    """
    generar_factura_xml
    """
    sale_id = 0

    if request.method == 'GET':
        sale_id = request.GET.get('sale_id')

    sale = SaleInvoice.objects.get(id=sale_id)
    products = ProductOnSaleInvoice.objects.filter(sale_invoice_id=sale_id)

    folder = os.path.dirname(os.path.abspath(__file__))

    invoice_template = os.path.join(folder, 'invoice_template.xml')
    src = Template(open(invoice_template).read())

    product_template_name = os.path.join(folder, 'product.xml')
    src_p = Template(open(product_template_name).read())

    product_list = []

    for product in products:
        data = {
            'id': str(product.product_id),
            'nombre_producto': str(product.product_name()),
            'cantidad': str(product.quantity),
            'iva': f'{product.unit_price * 0.19}',
            'sin_iva': f'{product.unit_price * 0.81}'
        }

        result = src_p.substitute(data)
        product_list.append(result)

    data = {
        # Invoice data
        'prefijo': 'CR',
        'consecutivo': 'CR1',
        'consec_desde': '000000',
        'consec_hasta': '999999',
        'CUFE': signing.dumps(str('hola'), key='3U8A#XFG,,u@Z)', compress=True),

        # Pharmacy data
        'nombre_empresa': 'Super Drogas',
        'NIT': '80526145',
        'departamento_empresa': 'Bogotá DC',
        'ciudad_empresa': 'Bogotá DC',
        'direccion_empresa': 'Cra. 80B 20 - 9',
        'pais_empresa': 'CO',

        # Client data
        'departamento_cliente': 'Valle',
        'ciudad_cliente': 'Cali',
        'direccion_cliente': 'Cll 9 # 4 - El Jordan',
        'pais_cliente': 'CO',
        'nombre_cliente': 'Luis Granja',
        'cedula_cliente': '1144091237',

        # Sale data
        'valor_final': str(sale.total_amount),
        'fecha_compra': str(sale.date),
        'iva': f'{sale.total_amount * 0.19}',
        'sin_iva': f'{sale.total_amount * 0.81}',
        'productos': '\n'.join(product_list)
    }

    result = src.substitute(data)

    response = HttpResponse(result, content_type='text/xml')
    response['Content-Disposition'] = 'attachment'
    response['Content-Disposition'] = 'filename="somefilename.xml"'
    return response


@csrf_exempt
def generar_factura_pdf(request):
    """
    generar_factura_pdf
    """
    sale_id = 0

    if request.method == 'GET':
        sale_id = request.GET.get('sale_id')

    folder = os.path.dirname(os.path.abspath(__file__))

    sale = SaleInvoice.objects.get(id=sale_id)
    products = ProductOnSaleInvoice.objects.filter(sale_invoice_id=sale_id)

    invoice_template = os.path.join(folder, 'invoice_template.html')
    src = Template(open(invoice_template).read())

    product_template_name = os.path.join(folder, 'product.html')
    src_p = Template(open(product_template_name).read())

    product_list = []

    for product in products:
        data = {
            'id': str(product.product_id),
            'nombre_producto': str(product.product_name()),
            'cantidad': str(product.quantity),
            'iva': f'{product.unit_price * 0.19}',
            'sin_iva': f'{product.unit_price * 0.81}',
            'valor_final_producto': str(product.unit_price)
        }

        result = src_p.substitute(data)
        product_list.append(result)

    filename = 'invoice.pdf'
    file = open(filename, "w+b")

    data = {
        # Invoice data
        'prefijo': 'CR',
        'consecutivo': 'CR1',
        'consec_desde': '000000',
        'consec_hasta': '999999',
        'CUFE': signing.dumps(str('hola'), key='3U8A#XFG,,u@Z)', compress=True),

        # Pharmacy data
        'nombre_empresa': 'Super Drogas',
        'NIT': '80526145',
        'departamento_empresa': 'Bogotá DC',
        'ciudad_empresa': 'Bogotá DC',
        'direccion_empresa': 'Cra. 80B 20 - 9',
        'correo_empresa': 'info@adidas.co',
        'telefono_empresa': '32054784',
        'pais_empresa': 'CO',

        # Client data
        'departamento_cliente': 'Valle',
        'ciudad_cliente': 'Cali',
        'direccion_cliente': 'Cll 9 # 4 - El Jordan',
        'pais_cliente': 'CO',
        'nombre_cliente': 'Luis Granja',
        'cedula_cliente': '1144091237',
        'correo_cliente': 'luis@mail.co',
        'telefono_cliente': '32054784',

        # Sale data
        'valor_final': str(sale.total_amount),
        'fecha_compra': str(sale.date),
        'iva': f'{sale.total_amount * 0.19}',
        'sin_iva': f'{sale.total_amount * 0.81}',
        'productos': '\n'.join(product_list)
    }

    result = src.substitute(data)
    pisa_status = pisa.CreatePDF(result, dest=file)

    file.close()

    fs = FileSystemStorage("")
    with fs.open(filename) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        return response


def sales_report(request):
    """
    :param request:
    :return: list with most bought products
    """
    if request.method == 'GET':
        schema_name = request.GET.get('schema_name')

    most_products = []
    response = {}

    with schema_context(schema_name):
        products = ProductOnSaleInvoice.objects.all().values('product_id').annotate(counter=Sum('quantity')).\
            order_by('-counter')

        for product in products:
            product_name = Product.objects.get(id=product['product_id']).name
            most_products.append({'name': product_name, 'quantity': str(product['counter'])})
        response.update({'most_products': most_products})

    return JsonResponse(response)


def general_pdf_report(request):
    """
    :param request:
    :return: list with most bought products
    """
    folder = os.path.dirname(os.path.abspath(__file__))

    sales_report_template = os.path.join(folder, 'report_templates/sales_report.html')
    src = Template(open(sales_report_template).read())

    product_report_template = os.path.join(folder, 'report_templates/producto.html')
    src_product = Template(open(product_report_template).read())

    schema_name = ''

    if request.method == 'GET':
        schema_name = request.GET.get('schema_name')

    filename = f'media/reports/{schema_name} - Sales Report.pdf'

    file = open(filename, "w+b")

    most_products = []
    response = {}

    with schema_context(schema_name):
        online_sales = SaleInvoice.objects.filter(sale_type='OL').count()
        response.update({'online_sales': online_sales})

        online_sales_total_amount = SaleInvoice.objects.filter(sale_type='OL').aggregate(Sum('total_amount'))
        response.update({'online_amount': online_sales_total_amount['total_amount__sum']})

        insitu_sales = SaleInvoice.objects.filter(sale_type='OS').count()
        response.update({'in_situ_sales': insitu_sales})

        insitu_sales_total_amount = SaleInvoice.objects.filter(sale_type='OS').aggregate(Sum('total_amount'))
        response.update({'in_situ_amount': insitu_sales_total_amount['total_amount__sum']})

        clients = User.objects.filter(rol='CM', is_active=True).count()
        response.update({'clientes_Activos': clients})

        sellers = User.objects.filter(rol='SL', is_active=True).count()
        response.update({'vendedores_Activos': sellers})

        product_list = []
        products = ProductOnSaleInvoice.objects.all().values('product_id').annotate(counter=Sum('quantity')).order_by('-counter')[:5]

        for product in products:
            product_name = Product.objects.get(id=product['product_id']).name
            most_products.append({'name': product_name, 'quantity': str(product['counter'])})

            cantidad = product['counter']
            data = {
                'nombre_producto': product_name,
                'cantidad': cantidad,
            }

            result = src_product.substitute(data)
            product_list.append(result)

        response.update({'most_products': most_products})
        response.update({'productos': ''.join(product_list)})
        response.update(({'nombre_empresa': get_tenant_info(schema_name)}))

    result = src.substitute(response)
    pisa_aux = pisa.CreatePDF(result, dest=file)
    file.close()

    fs = FileSystemStorage("")
    with fs.open(filename) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response
