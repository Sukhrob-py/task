from django.db import models

from product.models import Product
from user.models import User


# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.quantity * int(self.product.price)

    def __str__(self):
        return f"{self.user.username}'s cart"
