from django.contrib import admin
from django.utils.safestring import mark_safe

from goods.models import Categories, Products

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('get_image', )
    # fields = ('name', 'slug', 'description', 'get_image', 'get_image2', 'price', 'discount', 'quantity', 'category')
    list_display = ('name', 'get_image', 'get_image2', 'price', 'discount', 'quantity', 'category')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width=50>')

    get_image.short_description = 'Main photo'

    def get_image2(self, obj):
        if obj.image2:
            return mark_safe(f'<img src={obj.image2.url} width=50>')

    get_image2.short_description = 'Hover-photo'
