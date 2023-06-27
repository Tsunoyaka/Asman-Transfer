from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import Auto, Driver
from .serializers import AutoSerializers, DriverSerializer


class AutoAPIVIew(APIView):
    @method_decorator(cache_page(20))
    def get(self, request):
        queryset = Auto.objects.all()
        serializer = AutoSerializers(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    

class DriverAPIView(APIView):
    @method_decorator(cache_page(20))
    def get(self, request):
        queryset = Driver.objects.all()
        serializer = DriverSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    