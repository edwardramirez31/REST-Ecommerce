from django.urls import path

from apps.products.api.views.general_views import (CategoryProductListView,
                                                   IndicatorListView,
                                                   MeasureUnitListView)
from apps.products.api.views.product_views import (
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView)

app_name = "products"

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='list_create'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),
         name='retrieve_update_destroy'),
    path('measure_units/', MeasureUnitListView.as_view(), name='measure_units'),
    path('category/', CategoryProductListView.as_view(), name='category'),
    path('indicator/', IndicatorListView.as_view(), name='indicator'),
]
