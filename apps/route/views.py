from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import Route
from .serializers import RouteSerializer

class RouteAPIVIew(APIView):
    @method_decorator(cache_page(20))
    def get(self, request):
        queryset = Route.objects.all()
        serializer = RouteSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
