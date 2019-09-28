"""
URL configuration for tenants

The 'urlpatterns' list routes URLs to views
"""

# Django
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

# Rest Auth
from rest_auth.views import PasswordResetConfirmView

# Vue project and tenant info
from .views import (
    # vue,
    TenantInfo
)


# Media files
urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    # Project apps
    url('api/accounts/', include('apps.accounts.urls')),
    url('api/inventory/', include('apps.inventory.urls')),
    url('api/sales/', include('apps.sales.urls')),
    url(r'^api/tenant-info/(?P<schema_name>.+)/$', TenantInfo.as_view()),

    # Rest Auth
    url(r'^api/password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^api/rest-auth/', include('rest_auth.urls')),

    # Vue project
    # url(r'^.*$', vue, name='vue'),
]
