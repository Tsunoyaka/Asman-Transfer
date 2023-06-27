from django.urls import path

from .views import RecallGetVIew, DocumentationAPIVIew, VideoAPIVIew, RecallCreateVIew


urlpatterns = [
    path('get-recall/', RecallGetVIew.as_view(), name='get-recall'),
    path('create-recall/', RecallCreateVIew.as_view(), name='create-recall'),
    path('get-documentation/', DocumentationAPIVIew.as_view(), name='get-documentation'),
    path('get-video/', VideoAPIVIew.as_view(), name='get-video')
]