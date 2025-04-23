from django.db.models import Q

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    q_objects = Q()
    for word in query.split():
        if len(word) > 2:
            q_objects |= Q(name__icontains=word)
            q_objects |= Q(description__icontains=word)
    goods = Products.objects.filter(q_objects)
    return goods
