import product.models as product

from django.contrib import admin
from django.contrib.admin import TabularInline
from django.db import models

from abstraction.admin import AdminImageWidget


class ProductImageInline(TabularInline):
    model = product.ProductImage
    extra = 0
    formfield_overrides = {
        models.ImageField: {
            'widget': AdminImageWidget
        }
    }


@admin.register(product.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ('group',)
    inlines = [ProductImageInline, ]
