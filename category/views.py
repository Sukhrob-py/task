from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import CategorySerializer, DiscountCategorySerializer
from .models import Category, DiscountCategory


class GetCategoryListApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=200)


class GetDiscountCategoryListApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        categories = DiscountCategory.objects.all()
        serializer = DiscountCategorySerializer(categories, many=True)
        return Response(serializer.data, status=200)
