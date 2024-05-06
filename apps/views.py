from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from apps.filters import ProductFilter
from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductListModelSerializer, ProductDetailModelSerializer


class CategoryListCreateAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryRetrieveUpdateDestroyAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    # filterset_fields = 'category',

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListModelSerializer
        return ProductDetailModelSerializer

# class ProductListCreateAPIView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductListModelSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = 'category',
#
#
# class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailModelSerializer
