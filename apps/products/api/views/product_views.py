from rest_framework import generics

from apps.products.models import Product
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(state=True)


        