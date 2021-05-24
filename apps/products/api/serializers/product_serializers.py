from dataclasses import fields

from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    ModelSerializer used to manipulate querysets from Product class.

    It excludes some base model fields, such as the state and dates.

    Methods:
    --------------------
    to_representation(self, instance)
        Takes the model instance and returns the JSON represention
        accessing the instance fields.
    """

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        # handling null values from the database
        category = instance.category.description if instance.category else ""
        measure_unit = instance.measure_unit.description if instance.measure_unit else ""

        return {
            'id': instance.pk,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image.name,
            'category': category,
            "measure_unit": measure_unit,
        }
