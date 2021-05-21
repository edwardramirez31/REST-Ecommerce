from rest_framework import serializers

from apps.products.models import CategoryProduct, Indicator, MeasureUnit


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
