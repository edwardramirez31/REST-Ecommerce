from apps.products.models import MeasureUnit, CategoryProduct, Indicator
from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        fields = ('id', 'description',)

class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        fields = ('id', 'description')

class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
