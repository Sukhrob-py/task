from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from product.models import Product
from .models import Cart
from .serializers import CartSerializer


class AddToCartApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        product_id = request.data["product_id"]
        quantity = request.data["quantity"]
        try:
            product = Product.objects.get(id=product_id)
            if int(quantity) and int(quantity) > 0:
                Cart.objects.create(
                    product=product, quantity=int(quantity), user=request.user
                )
                return Response(
                    {"response": "Product added to Cart successfuly"}, status=201
                )
            return Response(
                {"error": "quantity error! (quantity must be integer and > 0)"}
            )
        except Exception as a:
            print(a)
            return Response({"error": "Something wrong"})


class GetUserCartApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        total = 0
        carts = Cart.objects.filter(user=request.user)
        for cart in carts:
            total += cart.total_price()
        serializer = CartSerializer(carts, many=True)
        return Response({"carts": serializer.data, "total": total}, status=200)


class DeleteProductCartApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        cart_id = request.data["cart_id"]
        carts = Cart.objects.filter(id=cart_id)
        carts.delete()
        return Response({"response": "Cart has been deleted!"})


class ClearCartApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        carts = Cart.objects.filter(user=request.user)
        carts.delete()
        return Response({"response": "Cart has been cleared!"})
