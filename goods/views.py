from django.shortcuts import render, get_object_or_404

from goods.models import Categories, Products


def catalog(request):
    context = {
        'title': 'Catalog',
        'goods': Products.objects.all(),
    }
    return render(request, 'goods/catalog.html', context)


def product(request, slug):
    context = {
        'title': 'Product',
        'product': get_object_or_404(Products, slug=slug),
    }
    return render(request, 'goods/product.html', context)

