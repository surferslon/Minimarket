from products.models import Category, Product
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = "__all__"
