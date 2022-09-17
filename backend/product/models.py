from django.db import models

from category.models import Category


class Product(models.Model):

    product_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}, {self.product_name}, {self.category.category_name}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
