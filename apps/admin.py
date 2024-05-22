from django.contrib import admin

from apps.models import Product, Category, ProductImage


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    min_num = 2


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ProductImageStackedInline]


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass
