from django.urls import path

from .views import TransferCreateView



urlpatterns = [
    path('create-transfer/', TransferCreateView.as_view(), name='create-transfer'),
]
