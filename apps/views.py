from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductListModelSerializer, ProductDetailModelSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all the category.",
        description="Return a list of all categories in the system.",
    )
)
class CategoryListCreateAPIView(ListAPIView):
    queryset = Category.objects.prefetch_related('products').order_by('id')
    serializer_class = CategoryModelSerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category').prefetch_related('productimage_set')
    serializer_class = ProductListModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['price', 'created_at']
    permission_classes = AllowAny,

    # v1
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = 'category', 'slug'

    # v2
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = {
    #     "price": ['lte']
    #     # "slug": ["contains"],
    #     # "description": ["contains"],
    # }
    #
    # # v3
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductFilter
    # ordering_fields = ['name']

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
# csrf_token
# product - (GET) product-list
