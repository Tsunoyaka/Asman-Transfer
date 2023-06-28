from django.urls import path

from .views import RouteAPIVIew


urlpatterns = [
    path('get-route/', RouteAPIVIew.as_view(), name='get-route'),
]