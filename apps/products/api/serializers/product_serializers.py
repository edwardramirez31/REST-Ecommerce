from rest_framework import serializers
from apps.products.models import Product

class ProductService(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
