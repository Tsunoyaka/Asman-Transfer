from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .serializers import TransferSerializer

class TransferCreateView(APIView):
    @swagger_auto_schema(request_body=TransferSerializer)
    def post(self, request):
        serializer = TransferSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Трансфер заполнен успешно!',
                status=status.HTTP_201_CREATED
            )
        
    