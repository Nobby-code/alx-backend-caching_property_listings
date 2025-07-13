from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
from django.utils.decorators import method_decorator
from .utils import get_all_properties
from .utils import get_redis_cache_metrics

# @cache_page(60 * 15)  # Cache for 15 minutes
# def property_list(request):
#     properties = Property.objects.all().values('id', 'title', 'description', 'price', 'location', 'created_at')
#     return JsonResponse(list(properties), safe=False)

def property_list(request):
    properties = get_all_properties()
    # return JsonResponse(properties, safe=False)
    return JsonResponse({"data": properties}, safe=False)

def cache_metrics(request):
    metrics = get_redis_cache_metrics()
    return JsonResponse(metrics)