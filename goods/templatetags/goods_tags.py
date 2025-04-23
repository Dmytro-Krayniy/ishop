from django import template
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library()


@register.simple_tag()
def tag_categories():
    categories_with_products = Categories.objects.filter(products__isnull=False).distinct()
    return categories_with_products

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query: dict = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
