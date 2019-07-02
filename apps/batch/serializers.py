from rest_framework import serializers
from .models import Batch


class BatchSerialize(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ('product',
                  'quantity',
                  'manufacturing_date',
                  'expiration_date')