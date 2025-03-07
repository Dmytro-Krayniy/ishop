from django.urls import path

from goods.scrapper import scrape_goods
from goods.views import catalog, product

app_name = 'goods'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('<slug:category_slug>/', catalog, name='catalog'),
    path('product/<int:product_id>', product, name='product'),
    path('product/<slug:slug>', product, name='product'),
    path('scrape/', scrape_goods, name='scrape'),
]

