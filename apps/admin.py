from django.contrib import admin

from apps.models import Product, Category, ProductImage


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    min_num = 2


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category']
    inlines = [ProductImageStackedInline]


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['name']

