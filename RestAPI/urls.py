from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import fetchAllMethod,searchMethod

urlpatterns = {
    path('fetchAll', fetchAllMethod, name="fetchAll"),
    path('search/<searchString>', searchMethod, name="search")
}

urlpatterns = format_suffix_patterns(urlpatterns)
