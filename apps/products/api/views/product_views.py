from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response

from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.products.models import Product


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(state=True)


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(state=True)

    def delete(self, request, pk):
        product = Product.objects.filter(pk=pk, state=True).first()
        if product:
            product.state = False
            product.save()
            return Response({"message: Successfully deleted"}, status=status.HTTP_200_OK)
        return Response({"message: Product Not found"}, status=status.HTTP_404_NOT_FOUND)
