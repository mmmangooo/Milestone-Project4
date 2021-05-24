from django.contrib import admin
from .models import Order, OrderLineItem

# Code adapted from Boutique Ado walkthrough project:
# https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/f5880efee43b3b9ea1276a09ca972f4588001c59/checkout/admin.py


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
# Making fields non-editable
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)
# Fields that can be edited
    fields = ('order_number', 'user_profile',
              'full_name', 'email',
              'phone_number', 'country', 'postcode',
              'town_or_city', 'street_address1',
              'street_address2', 'county', 'date',
              'delivery_cost', 'order_total', 'grand_total',)

    list_display = ('order_number', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
