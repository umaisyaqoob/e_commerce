from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)
