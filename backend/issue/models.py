from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from category.models import Category
from product.models import Product

User = get_user_model()



class Issue(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, null=True, related_name='user_report')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT, null=True, blank=True)
    message = models.TextField(max_length=255, blank=True, null=True)
    suggestions = models.TextField(max_length=255, blank=True, null=True)
    delay_estimation = models.CharField(max_length=32, blank=True, null=True)
    image = models.ImageField(blank=True)
    status = models.IntegerField(
        verbose_name='status',
        choices=(
            (0, 0),
            (1, 1),
        ),
        default= 0,
        null=True

    )
    gps_coordinates = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}, USERNAME: {self.user.username}, ROLE {self.user.role}   WALLET : {self.user.wallet_address},  GPS : {self.gps_coordinates}, STATUS :{self.status}'

    class Meta:
        verbose_name = 'issue'
        verbose_name_plural = 'issues'

