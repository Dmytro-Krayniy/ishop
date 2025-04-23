from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from goods.models import Categories, Products
from goods.utils import q_search


def catalog(request, category_slug='all'):
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug != 'all':
        goods = Products.objects.filter(category__slug=category_slug)
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.all()
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 4)
    page_number = request.GET.get("page")
    current_page = paginator.get_page(page_number)

    context = {
        'title': 'Catalog',
        'page_obj': current_page,
        'category_slug': category_slug,
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

