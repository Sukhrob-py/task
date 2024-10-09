from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to="category")

    def __str__(self):
        return self.name


class DiscountCategory(models.Model):
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to="category")
    discount = models.IntegerField()
    desc = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
