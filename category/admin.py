from django.contrib import admin

# Register your models here.
from .models import Category,DiscountCategory
admin.site.register(Category)
admin.site.register(DiscountCategory)