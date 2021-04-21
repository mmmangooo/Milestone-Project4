from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Toy, Category
from django.db.models import Q


def all_toys(request):
    """ A view to show all toys in the database,
        sort, show by category and search them"""

    toys = Toy.objects.all()
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
            toys = toys.filter(category_name_in=categories)
            categories = Category.objects.filter(name_in=categories)

        if request.GET:
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey


#           if 'direction'



    context = {
        'toys': toys,
        'current_categories': categories,
        'search_term': query,
   #     'current_sorting': current_sorting,
    }

    return render(request, 'toys/toys.html', context)
