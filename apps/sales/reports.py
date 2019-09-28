# Django Tenants
from django_tenants.utils import schema_context

# Django
from django.http import JsonResponse
from django.db.models import Sum
from apps.sales.models.product_on_sale_model import ProductOnSaleInvoice
from apps.sales.models.sale_invoice_model import SaleInvoice
from apps.inventory.models.product_model import Product


def get_products_report(request):
    if request.method == 'GET':
        schema_name = request.GET.get('schema_name')

    response = {}
    nombres = []
    cantidades = []

    with schema_context(schema_name):
        products = ProductOnSaleInvoice.objects.all().values('product_id').annotate(counter=Sum('quantity')).order_by('-counter')[:5]

        for product in products:
            product_name = Product.objects.get(id=product['product_id']).name
            cantidad = product['counter']
            nombres.append(str(product_name))
            cantidades.append(str(cantidad))
        response.update({'nombres': '|'.join(nombres), 'cantidad': ','.join(cantidades)})

    return JsonResponse(response)


def get_sales_report(request):

    if request.method == 'GET':
        schema_name = request.GET.get('schema_name')

    response = {}
    valores = []

    with schema_context(schema_name):
        for i in range(1, 31):
            sales = SaleInvoice.objects.filter(date__day=i, date__month=9)
            valor_total = 0

            for sale in sales:
                valor_total += sale.total_amount
            valores.append(str(valor_total))

        response.update({'valores': ','.join(valores)})

    return JsonResponse(response)
