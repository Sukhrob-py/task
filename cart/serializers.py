from rest_framework.serializers import ModelSerializer, Serializer

from .models import Cart
from product.serializers import ProductSerializer


class CartSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = ["id", "quantity", "product", "user"]
