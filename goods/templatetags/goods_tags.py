from django import template

from goods.models import Categories

register = template.Library()


@register.simple_tag()
def tag_categories():
    categories_with_products = Categories.objects.filter(products__isnull=False).distinct()
    return categories_with_products
