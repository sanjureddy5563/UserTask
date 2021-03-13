from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=25)
    product_price = models.CharField(max_length=6)
    product_type = models.CharField(max_length=30)
    product_location = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name