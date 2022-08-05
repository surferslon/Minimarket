from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from rest_framework.generics import ListAPIView


class ProductListView(ListAPIView):
    queryset = Product.objects.all().prefetch_related("categories")
    serializer_class = ProductSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
