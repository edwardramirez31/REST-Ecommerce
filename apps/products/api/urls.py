from django.urls import path

from apps.products.api.views.general_views import (CategoryProductListView,
                                                   IndicatorListView,
                                                   MeasureUnitListView)
from apps.products.api.views.product_views import (ProductCreateAPIView,
                                                   ProductDeleteAPIView,
                                                   ProductListView,
                                                   ProductRetrieveAPIView,
                                                   ProductUpdateAPIView)

app_name = "products"

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', ProductRetrieveAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='update'),
    path('measure_units/', MeasureUnitListView.as_view(), name='measure_units'),
    path('category/', CategoryProductListView.as_view(), name='category'),
    path('indicator/', IndicatorListView.as_view(), name='indicator'),
]
