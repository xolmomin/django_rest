import uuid

from django.contrib.postgres.functions import RandomUUID
from django.db.models import Model, CASCADE, ImageField, CharField, SlugField, FloatField, DateTimeField, \
    ForeignKey, UUIDField
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class CreatedBaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class SlugBaseModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)


class Category(SlugBaseModel):
    id = UUIDField(primary_key=True, db_default=RandomUUID(), editable=False)
    image = ImageField(null=True, blank=True, upload_to='categories/image/%Y/%m/%d/')


class Product(CreatedBaseModel, SlugBaseModel):
    id = UUIDField(primary_key=True, db_default=RandomUUID(), editable=False)
    price = FloatField(default=0)
    description = CKEditor5Field(null=True, blank=True)
    category = ForeignKey('apps.Category', CASCADE, related_name='products')


class ProductImage(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = ImageField(upload_to='products/image/%Y/%m/%d/')
    product = ForeignKey('apps.Product', CASCADE)
