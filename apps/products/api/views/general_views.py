from apps.base.api import BaseListAPIView
from apps.products.api.serializers.general_serializers import (MeasureUnitSerializer, 
IndicatorSerializer, 
CategoryProductSerializer)


class MeasureUnitListView(BaseListAPIView):
    serializer_class = MeasureUnitSerializer


class CategoryProductListView(BaseListAPIView):
    serializer_class = CategoryProductSerializer


class IndicatorListView(BaseListAPIView):
    serializer_class = IndicatorSerializer

