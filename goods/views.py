from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from goods.models import Categories, Products


def catalog(request, category_slug=None):
    if category_slug:
        goods = Products.objects.filter(category__slug=category_slug)
    else:
        goods = Products.objects.all()

    paginator = Paginator(goods, 4)
    page_number = request.GET.get("page")
    current_page = paginator.get_page(page_number)

    context = {
        'title': 'Catalog',
        'page_obj': current_page,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, slug=None, product_id=None):
    if product_id:
        prod = get_object_or_404(Products, id=product_id)
    else:
        prod = get_object_or_404(Products, slug=slug)
    context = {
        'title': 'Product',
        'product': prod,
    }
    return render(request, 'goods/product.html', context)

