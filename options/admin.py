import options.models as option

from django.contrib import admin


@admin.register(option.Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(option.Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    autocomplete_fields = ('manufacturer',)


@admin.register(option.Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    autocomplete_fields = ('group',)


@admin.register(option.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    autocomplete_fields = ('category',)


@admin.register(option.ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    autocomplete_fields = ('subcategory',)
