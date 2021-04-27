from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Toy, Category, Campaign
from django.db.models import Q


def all_toys(request):
    """ A view to show all toys in the database,
        sort, show by category and search them"""

    toys = Toy.objects.all()
    campaign = Campaign.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, "No search qriteria entered")
                return redirect(reverse('toys'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            toys = toys.filter(queries)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            toys = toys.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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
        'campaign': campaign,
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
