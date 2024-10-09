from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import ProductSerializer
from .models import Product


class GetProductListApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=200)


class NewProductsListApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        products = Product.objects.all()[::-1]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=200)


class VegetablesListApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        products = Product.objects.filter(category__name="Vegetables & Fruits")
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=200)


class SearchProductsApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        key = request.data["key"]
        if len(key) >= 3:
            products = Product.objects.filter(title__icontains=key)
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=200)


class ProductsListByCategoryApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        id = request.data["id"]
        try:
            products = Product.objects.filter(category__id=int(id))
        except:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=200)
