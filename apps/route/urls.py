from django.urls import path

from .views import RouteAPIVIew, Send
from . import views


urlpatterns = [
    path('get-route/', RouteAPIVIew.as_view(), name='get-route'),
]