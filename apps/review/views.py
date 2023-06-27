from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


from .models import Recall, Documentation, Video
from .serializers import RecallSerializer, DocumentationSerializer, VideoSerializer


class RecallGetVIew(APIView):
    @method_decorator(cache_page(20))
    def get(self, request):
        queryset = Recall.objects.all()
        serializer = RecallSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    

class RecallCreateVIew(APIView):
    @swagger_auto_schema(request_body=RecallSerializer)
    def post(self, request):
        serializer = RecallSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Отзыв успешно оставлен!',
                status=status.HTTP_201_CREATED
            )

class DocumentationAPIVIew(APIView):
    @method_decorator(cache_page(20))
    def get(self, request):
        queryset = Documentation.objects.all()
        serializer = DocumentationSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    

class VideoAPIVIew(APIView):
    @method_decorator(cache_page(20))
    def get(self, request):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)