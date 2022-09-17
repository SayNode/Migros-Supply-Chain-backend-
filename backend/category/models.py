from django.db import models

class Category(models.Model):

    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}, {self.category_name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
