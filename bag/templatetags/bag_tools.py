from django import template


register = template.Library()


# Calculation of total price available in templates
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
