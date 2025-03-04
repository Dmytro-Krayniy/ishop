from decimal import Decimal

from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    objects = models.Manager

    class Meta:
        db_table = 'category'
        verbose_name = 'категорія'
        verbose_name_plural = 'категорії'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='опис')
    image = models.ImageField(upload_to='product_images', blank=True, null=True, verbose_name='зображення')
    image2 = models.ImageField(upload_to='product_images', blank=True, null=True, verbose_name='зображення2')
    price = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name='ціна')
    discount = models.DecimalField(default=0.0, max_digits=4, decimal_places=2, verbose_name='знижка, %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='кількість')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='категорія',
                                 related_name='products')

    class Meta:
        db_table = 'product'
        verbose_name = 'товар'
        verbose_name_plural = 'товари'

    @property
    def sell_price(self):
        return round(self.price * Decimal(100 - self.discount) / Decimal(100.00), 2)

    def display_id(self):
        return f'{self.id:05}'

    def __str__(self):
        return self.name
