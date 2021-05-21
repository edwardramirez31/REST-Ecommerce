from django.contrib import admin

from apps.products.models import (CategoryProduct, Indicator, MeasureUnit,
                                  Product)


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


# Register your models here.
admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct, CategoryAdmin)
admin.site.register(Indicator)
admin.site.register(Product)
