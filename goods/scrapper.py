import requests
import json
from bs4 import BeautifulSoup
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from goods.models import Products, Categories

URL = 'https://kleo.ua/ua/outlet'


def scrape_goods(request):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    goods = []
    goods_json = []
    i = 0
    for item in soup.select('.items-wr'):
        i += 1
        print(f'Scrapping. Object {i}...')
        name = ''
        try:
            # good = Products(
            name = item['data-title']
            description = item.select_one('.items-title').get_text(strip=True)
            image = item.select_one('.add-photo>img').get('src')
            image2 = item.select_one('.add-photo').get('data-link')
            price = int(item['data-price'])
            discount = round((1 - price / int(item.select_one('.items-price').get_text().split()[0])) * 100, 0)
            category = item['data-category']
            # )
            try:
                cat = Categories.objects.get(name=category)
            except ObjectDoesNotExist:
                cat = Categories.objects.get(name='інше')
            goods.append(
                Products(name=name, description=description, image=image, price=price, discount=discount,
                         category=cat))
            goods_json.append(dict(name=name, description=description, image=image, image2=image2, price=price,
                                   discount=discount, category=category))
        except Exception:
            print(f'object {name} skipped')

    with open('goods.json', 'w', encoding='utf-8') as json_file:
        json.dump(goods_json, json_file, ensure_ascii=False, indent=4)
    # Products.objects.bulk_create(goods)
    print(f'Scraped {len(goods)} items.')

    data = {
        'title': 'Головна',
        'content': f'Scraped {len(goods)} items.',
        'categories': Categories.objects.all()
    }
    return render(request, 'main/index.html', context=data)

if __name__ == '__main__':
    scrape_goods()
