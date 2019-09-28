"""
Vue project

Vue project index built
"""

# Django
# from django.shortcuts import render
from django.http import HttpResponse

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Pharmacy serializers
from apps.pharmacies.serializers import PharmacySerializer

# Utilities
from .utilities import get_tenant_info


def vue(request):
    """
    vue return the Vue index
    """
    # return render(request, template_name='index.html')
    return HttpResponse('Vue project')


class TenantInfo(APIView):
    """
    tenant_info view returns the tenant's information by schema name
    """
    def get(self, request, *args, **kwargs):
        """
        get return the tenant's information in the GET method
        """
        schema_name = kwargs.get('schema_name', 'public')
        pharmacy = get_tenant_info(schema_name)
        data = PharmacySerializer(pharmacy).data
        return Response(data)
