from rest_framework.serializers import ModelSerializer

from .models import Category,DiscountCategory


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class DiscountCategorySerializer(ModelSerializer):
    class Meta:
        model = DiscountCategory
        fields = "__all__"
