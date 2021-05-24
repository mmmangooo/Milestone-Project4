from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from toys.models import Toy

# Code adapted from Boutique Ado walkthrough project:
# https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/f5880efee43b3b9ea1276a09ca972f4588001c59/bag/views.py


def view_bag(request):
    """
    View to show the bag contents page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    View to add a toy with a specified quantity to the shopping bag
    """
    toy = get_object_or_404(Toy, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # Increasing the quantity of the toy in the bag,
    # if the used adds another of a toy already in the bag
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated quantity of {toy.name} to {bag[item_id]}')
    # Adding a toy to the bag when that toy is not already in the user's bag
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {quantity} {toy.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    View to adjust the quantity of a product in the bag
    """
    toy = get_object_or_404(Toy, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    # Updating the quantity of a toy in the bag when there is still
    # one or more of the toys left in the bag after quantity update
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated quantity of {toy.name} to {quantity}')

    # Updating the quantity when there is none of
    # that toy left in the bag after update
    else:
        bag.pop(item_id)
        messages.success(request, f'{toy.name} removed from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    View to remove item from shopping bag
    """
    # Try removing the toy from the bag and returning a success
    # message to the user on delete completed
    try:
        toy = get_object_or_404(Toy, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'{toy.name} removed from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    # Returning an error message to the user when delete is not successful
    except Exception as e:
        messages.error(
            request, f'Something went wrong, item was not removed: {e}')
        return HttpResponse(status=500)
