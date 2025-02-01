from django.shortcuts import render

from goods.models import Categories, Products

goods_lst = [
    {'image1': 'images/product1.jpg',
     'image2': 'images/product1-hover.jpg',
     'name': "Men's underpants",
     'description': "The best Men's underpants I have ever seen",
     'price': 100},
    {'image1': 'images/product2.jpg',
     'image2': 'images/product2_2.jpg',
     'name': "Lace Thongs",
     'description': "The best Lace Thongs I have ever seen",
     'price': 120},
    {'image1': 'images/product3.jpg',
     'image2': 'images/product3_3.jpg',
     'name': "Cotton Boxer Shorts",
     'description': "The best Cotton Boxer Shorts I have ever seen",
     'price': 80},
]


def catalog(request):
    context = {
        'title': 'Catalog',
        'goods': Products.objects.all(),
        'categories': Categories.objects.all()
    }
    return render(request, 'goods/catalog.html', context)


def product(request, slug):
    context = {
        'title': 'Catalog',
        # 'goods': Products.objects.get_or_404(),
        'categories': Categories.objects.all()
    }
    return render(request, 'goods/product.html', context)

