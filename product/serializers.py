from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Product


class ProductSerializer(ModelSerializer):
    category_title = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "title", "price", "old_price", "photo", "category_title"]

    def get_category_title(self, obj):
        return obj.category.name
