from rest_framework import generics

from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.products.models import Product


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(state=True)


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
