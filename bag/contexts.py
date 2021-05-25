from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from toys.models import Toy

# Code adapted from the Boutique Ado walkthrough project:
# https://github.com/ckz8780/boutique_ado_v1/blob/master/bag/contexts.py


# Function for handling shopping bag calculations of quantity, prices,
# delivery cost and grand total
def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        # Calculate quantity and total price when a toy is added to the bag
        if isinstance(item_data, int):
            toy = get_object_or_404(Toy, pk=item_id)
            price = toy.get_price()
            total += item_data * price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'toy': toy,
            })
        else:
            toy = get_object_or_404(Toy, pk=item_id)

    # Calculate delivery cost, checking if the total for
    # toys bought is over the limit for free delivery
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(
            settings.STANDARD_DELIVERY_COST)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Calculate bag total including both total price for toys and delivery
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context
