from django.contrib import admin
from .models import Category, Toy


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ToyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'sku',
        'price',
        'description',
        'rating',
        'image'
    )


admin.site.register(Toy, ToyAdmin)
admin.site.register(Category, CategoryAdmin)
