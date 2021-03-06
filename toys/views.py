from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Toy, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import ToyForm

# Code adapted from Boutique Ado walkthrough project:
# https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/f5880efee43b3b9ea1276a09ca972f4588001c59/products/views.py


def all_toys(request):
    """ A view to show all toys in the database,
        sort, show by category and search them"""

    toys = Toy.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        # Handling returning result when user has made a search for toys
        if 'query' in request.GET:
            query = request.GET['query']
            # Handling if user clicked search without entering search criteria
            if not query:
                messages.error(request, "No search qriteria entered")
                return redirect(reverse('toys'))

            # Filtering db query by user's search criteria,
            # in name and description of toy
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            toys = toys.filter(queries)

        # Handling returning toys in the right category when user
        # has chosen a category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            toys = toys.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handling returning toys sorted by the criteria the user
        # has chosen, when the user has chosen any sort criteria
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                toys = toys.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            toys = toys.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'toys': toys,
        'categories': categories,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'toys/toys.html', context)


def toy_details(request, toy_id):
    """ A view to show individual toy details"""

    toy = get_object_or_404(Toy, pk=toy_id)

    context = {
        'toy': toy,
    }

    return render(request, 'toys/toy_details.html', context)


@login_required
def add_toy(request):
    """
    A view to add a toy to the store
    """
    # Stopping a user from accessing this functionality if
    # they are not logged in with superuser credentials
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    # Handling functionality of add a btoy to the db, or returning an
    # error message if add toy did not succeed
    if request.method == 'POST':
        form = ToyForm(request.POST, request.FILES)
        if form.is_valid():
            toy = form.save()
            messages.success(request, 'Successfully added toy!')
            return redirect(reverse('toy_details', args=[toy.id]))
        else:
            messages.error(
                request, 'Sorry, something went wrong. \
                    The toy was not added to the store')
    # Rendering an empty add toy form
    else:
        form = ToyForm()

    template = 'toys/add_toy.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_toy(request, toy_id):
    """
    A view to edit a toy in the store
    """
    # Stopping a user from accessing this functionality if
    # they are not logged in with superuser credentials
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    toy = get_object_or_404(Toy, pk=toy_id)

    # Handling functionality of edit a toy to the db, or returning an
    # error message if edit toy did not succeed
    if request.method == 'POST':
        form = ToyForm(request.POST, request.FILES, instance=toy)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated toy!')
            return redirect(reverse('toy_details', args=[toy.id]))
        else:
            messages.error(
                request, 'Sorry, something went wrong. \
                    The toy was not updated.')

    # Rendering an edit form for the specific toy and message
    # to the user about which toy they are editing
    else:
        form = ToyForm(instance=toy)
        messages.info(request, f'You are editing {toy.name}')

    template = 'toys/edit_toy.html'
    context = {
        'form': form,
        'toy': toy,
    }

    return render(request, template, context)


@login_required
def confirm_delete_toy(request, toy_id):
    """
    A view for rendering a template where deletion is confirmed or cancelled
    """
    # Stopping a user from accessing this functionality if
    # they are not logged in with superuser credentials
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    # Getting the specific toy from the db
    toy = get_object_or_404(Toy, pk=toy_id)
    context = {
        'toy': toy,
    }

    template = 'toys/confirm_delete_toy.html'

    return render(request, template, context)


@login_required
def delete_toy(request, toy_id):
    """
    Delete a toy from the store
    """

    # Stopping a user from accessing this functionality if
    # they are not logged in with superuser credentials
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    # Getting the specific toy and deleting it from the db
    toy = get_object_or_404(Toy, pk=toy_id)
    toy.delete()
    messages.success(request, f'{toy.name} deleted from the store.')
    return redirect(reverse('toys'))
