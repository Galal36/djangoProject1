from django.db import models
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
# Create your models here.
