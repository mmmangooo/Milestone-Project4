from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from toys.models import Toy


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            toy = get_object_or_404(Toy, pk=item_id)
            total += item_data * toy.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'toy': toy,
            })
        else:
            toy = get_object_or_404(Toy, pk=item_id)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(
            settings.STANDARD_DELIVERY_COST)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

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
