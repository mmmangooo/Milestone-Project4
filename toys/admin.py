from django.contrib import admin
from .models import Category, Toy, Campaign


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


class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'toy',
        'price',
    )


admin.site.register(Toy, ToyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Campaign, CampaignAdmin)
