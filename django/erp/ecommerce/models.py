from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    create_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    no = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    image = models.CharField(max_length=1000, null=True)
    unit_price = models.DecimalField(max_digits=100, decimal_places=3)

    def __str__(self):
        return f"{self.no} - {self.brand} - {self.description} - {self.size}"


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    create_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name} - {self.description}"