from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def cals_subtotal(price, quantity):
    return price * quantity
