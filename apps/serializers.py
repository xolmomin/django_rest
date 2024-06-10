from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product, ProductImage


class CategoryModelSerializer(ModelSerializer):
    # product_count = SerializerMethodField()

    class Meta:
        model = Category
        fields = 'id', 'name', 'slug', 'image' # , 'product_count'

    # def get_product_count(self, obj: Category):
    #     return obj.products.count()


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = 'id', 'image'


class ProductListModelSerializer(ModelSerializer):
    category = CategoryModelSerializer()
    images = ProductImageModelSerializer(source='productimage_set', many=True, read_only=True)

    class Meta:
        model = Product
        fields = 'id', 'name', 'price', 'description', 'category', 'images'
        # exclude = 'created_at', 'updated_at', 'description'

    def vowel_count(self, obj: Product):
        return sum(True for i in obj.description if i not in 'aioue')

    # def to_representation(self, instance: Product):
    #     represent = super().to_representation(instance)
    #     represent['category'] = CategoryModelSerializer(instance.category, context={'request': self.context['request']}).data
    #     return represent


class ProductDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = 'updated_at',

    def to_representation(self, instance: Product):
        represent = super().to_representation(instance)
        represent['category'] = CategoryModelSerializer(instance.category).data
        return represent
