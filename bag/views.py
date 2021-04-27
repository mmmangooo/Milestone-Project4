from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from toys.models import Toy


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

    if item_id in list(bag.keys()):
        bag[item_id] = quantity
        messages.success(
            request, f'Updated quantity of {toy.name} to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {toy.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    View to adjust the quantity of a product in the bag
    """
    toy = get_object_or_404(Toy, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated quantity of {toy.name} to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'{toy.name} removed from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    View to remove item from shopping bag
    """

    try:
        toy = get_object_or_404(Toy, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'{toy.name} removed from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request, f'Something went wrong, item was not removed: {e}')
        return HttpResponse(status=500)
