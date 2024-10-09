from django.db import models

from category.models import Category


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=128)
    price = models.CharField(max_length=64)
    old_price = models.CharField(max_length=64)
    photo = models.ImageField(upload_to="product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title
