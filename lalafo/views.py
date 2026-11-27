from itertools import product

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Lalafo, Category


def hello(request):
    categories = Category.objects.all()

    return render(request, 'home.html', {
        'categories': categories,
    })



# def my_transport(request):
#     products = Lalafo.objects.filter(category__title='Транспорт')
#     return render(request, 'products.html', {
#         'products': products,
#     })
#
# def nedvijimost(request):
#     products = Lalafo.objects.filter(category__title='Недвижимость')
#     return render(request, 'products.html', {
#         'products': products,
#     })

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Lalafo.objects.filter(category=category)
    return render(request, 'products.html', {
        'products': products,
        'category': category,
    })