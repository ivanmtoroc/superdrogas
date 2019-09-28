"""
Project utilities
"""

# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Django Tenants
from django_tenants.utils import schema_context

# Accounts models
from apps.accounts.models import User

# Pharmacies models
from apps.pharmacies.models import Pharmacy

# Python
import random
import string


def send_admin_email(username, password, user_email):
    """
    send_admin_email send admin credentials
    """
    subject = f'Welcome to Super Drogas!'
    content = render_to_string(
        'tenants/new_user.html',
        {'username': username, 'password': password}
    )
    from_email = 'Super Drogas <superdrogas.contacto@gmail.com>'

    email = EmailMultiAlternatives(subject, content, from_email, [user_email])
    email.attach_alternative(content, "text/html")
    email.send()


def get_tenant_info(schema_name):
    """
    get_tenant_info return the first tenant object by schema_name
    """
    with schema_context(schema_name):
        return Pharmacy.objects.filter(schema_name=schema_name).first()


def random_password(string_length=20):
    """
    random_password generate a random string of fixed length
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))
