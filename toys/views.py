from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Toy, Category


def all_toys(request):
    """ This is a view to show all toys in the database"""

    toys = Toy.objects.all()

    context = {
        'toys': toys,
    }

    return render(request, 'toys/toys.html', context)
