"""
Users URLs

The 'urlpatterns' list routes URLs to viewsets
"""

# Django
from django.conf.urls import url

# Django Rest Framework
from rest_framework import routers

# Accounts viewsets
from .viewsets import (
    UserViewSet,
    LoginView
)

from .utilities import get_backup, get_tenant_report


ROUTER = routers.DefaultRouter()

ROUTER.register(r'users', UserViewSet)

urlpatterns = [
    url('login/', LoginView.as_view(), name='login'),
    url('tenant_backup/', get_backup, name='tenant_backup'),
    url('tenant_report/', get_tenant_report, name='tenant_report'),
]

urlpatterns += ROUTER.urls
