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
    vendor = models.CharField(max_length=100,null=True)
    original_price = models.BigIntegerField(null=True)
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
    quantity = models.IntegerField(null=True)
    total_price = models.IntegerField(null=True)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    # cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    payment = models.CharField(max_length=50)
    quantity = models.IntegerField(null=True)
    price = models.BigIntegerField(null=True)
    status = models.CharField(max_length=50, null=True)
    order_date = models.DateField(auto_now_add=True)