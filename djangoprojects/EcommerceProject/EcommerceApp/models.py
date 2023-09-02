from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CategoryModel(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField()

class ProductModel(models.Model):
    product_name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.BigIntegerField()
    mfg_date = models.DateField()
    image = models.ImageField(upload_to='productImages/')

class CustomerModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    address = models.TextField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)

class CartModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)