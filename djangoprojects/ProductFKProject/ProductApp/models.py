from django.db import models

# Create your models here.
class CategoriesModel(models.Model):
    category_name = models.CharField(max_length=50)

class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_quantity = models.IntegerField()
    product_price = models.IntegerField()
    product_category = models.ForeignKey(CategoriesModel,on_delete=models.CASCADE)
    product_manufacture_date = models.DateField()
    product_image = models.ImageField(upload_to='image/')