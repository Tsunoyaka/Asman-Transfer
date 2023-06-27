from django.urls import path

from .views import AutoAPIVIew, DriverAPIView


urlpatterns = [
    path('get-auto/', AutoAPIVIew.as_view(), name='get-auto'),
    path('get-driver/', DriverAPIView.as_view(), name='get-driver'),
]