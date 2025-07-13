from django.urls import path
from .views import property_list
from .views import cache_metrics

urlpatterns = [
    path('', property_list, name='property-list'),
    path('metrics/', cache_metrics, name='cache-metrics'),
]