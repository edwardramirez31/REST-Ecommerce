from django.urls import path
from apps.products.api.views.general_views import (MeasureUnitListView, 
CategoryProductListView,
IndicatorListView)

app_name = "products"

urlpatterns = [
    path('measure_units/', MeasureUnitListView.as_view(), name='measure_units'),
    path('category/', CategoryProductListView.as_view(), name='category'),
    path('indicator/', IndicatorListView.as_view(), name='indicator'),
]