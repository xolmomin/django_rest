from django.db.models import Model, CASCADE, CharField, SlugField, FloatField, TextField, DateTimeField, ForeignKey
from django.utils.text import slugify


class CreatedBaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class SlugBaseModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(SlugBaseModel):
    pass


class Product(CreatedBaseModel, SlugBaseModel):
    price = FloatField(default=0)
    description = TextField(null=True, blank=True)
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
